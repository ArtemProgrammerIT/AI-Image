import asyncio
import base64
import json
import random
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional
from urllib.parse import urlparse
from flask import Flask, render_template, request
import websockets
from deep_translator import GoogleTranslator

app = Flask(__name__)

class SDXLStyle(Enum):
    """Available SDXL styles"""
    NO_STYLE = "(No style)"
    CINEMATIC = "Cinematic"
    PHOTOGRAPHIC = "Photographic"
    ANIME = "Anime"
    MANGA = "Manga"
    DIGITAL_ART = "Digital Art"
    PIXEL_ART = "Pixel art"
    FANTASY_ART = "Fantasy art"
    NEONPUNK = "Neonpunk"
    THREE_D_MODEL = "3D Model"

    @classmethod
    def get_by_index(cls, index: int):
        styles = list(cls)
        if 0 <= index < len(styles):
            return styles[index]
        return cls.NO_STYLE

class SDXLException(Exception):
    pass

class ConnectionError(SDXLException):
    pass

class ResponseError(SDXLException):
    pass

class TranslationError(SDXLException):
    pass

@dataclass
class SDXLConfig:
    ws_url: str = "wss://google-sdxl.hf.space/queue/join"
    timeout: int = 60
    max_size: int = 10 * 1024 * 1024  # 10MB
    max_queue: int = 2048
    fn_index: int = 2
    translate_from: str = "ru"
    translate_to: str = "en"
    auto_translate: bool = True

    def __post_init__(self):
        result = urlparse(self.ws_url)
        if not all([result.scheme, result.netloc]):
            raise ValueError("Invalid WS URL")

class SDXLClient:
    def __init__(self, config: SDXLConfig):
        self.config = config
        self._session_hash: Optional[str] = None
        self._translator = None
        if self.config.auto_translate:
            self._translator = GoogleTranslator(
                source=self.config.translate_from, target=self.config.translate_to
            )

    @staticmethod
    def _generate_session_hash(length: int = 10) -> str:
        return "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=length))

    async def _translate_text(self, text: str) -> str:
        if not text or not self.config.auto_translate:
            return text
        try:
            translated = self._translator.translate(text)
            return translated
        except Exception as e:
            raise TranslationError(f"Translation failed: {e}")

    async def _validate_base64_image(self, image_data: str) -> bool:
        try:
            if not image_data.startswith("data:image/jpeg;base64,"):
                return False
            base64_str = image_data.split(",")[1]
            base64.b64decode(base64_str)
            return True
        except Exception:
            return False

    async def generate(self, prompt: str, negative_prompt: str = "", cfg_scale: float = 7.5, style: SDXLStyle = SDXLStyle.NO_STYLE) -> List[str]:
        try:
            translated_prompt = await self._translate_text(prompt)
            translated_negative = await self._translate_text(negative_prompt)

            async with websockets.connect(
                self.config.ws_url,
                max_size=self.config.max_size,
                max_queue=self.config.max_queue,
            ) as websocket:
                message = await asyncio.wait_for(websocket.recv(), timeout=self.config.timeout)
                data = json.loads(message)

                if data.get("msg") != "send_hash":
                    raise ResponseError("Expected send_hash message")

                self._session_hash = self._generate_session_hash()
                await websocket.send(json.dumps({
                    "fn_index": self.config.fn_index,
                    "session_hash": self._session_hash,
                }))

                while True:
                    message = await asyncio.wait_for(websocket.recv(), timeout=self.config.timeout)
                    data = json.loads(message)
                    if data.get("msg") == "send_data":
                        break

                await websocket.send(json.dumps({
                    "data": [
                        translated_prompt,
                        translated_negative,
                        cfg_scale,
                        style.value,
                    ],
                    "event_data": None,
                    "fn_index": self.config.fn_index,
                    "session_hash": self._session_hash,
                }))

                await asyncio.wait_for(websocket.recv(), timeout=self.config.timeout)  # Progress response
                response = await asyncio.wait_for(websocket.recv(), timeout=self.config.timeout)  # Result response

                response_data = json.loads(response)
                output_data = response_data.get("output", {})
                data_array = output_data.get("data", [])

                if not data_array or not isinstance(data_array, list):
                    raise ResponseError("Invalid response structure")

                images = [
                    img for img in data_array[0]
                    if isinstance(img, str) and await self._validate_base64_image(img)
                ]

                if not images:
                    raise ResponseError("No valid images in response")

                return images

        except asyncio.TimeoutError:
            raise ConnectionError("Connection timeout")
        except websockets.exceptions.ConnectionClosed as e:
            raise ConnectionError(f"Connection closed unexpectedly: {e}")
        except SDXLException:
            raise
        except Exception as e:
            raise SDXLException(f"Unexpected error: {e}")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', image_url=None)

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form.get('prompt')
    style_index = int(request.form.get('style_index', 0))

    # Получаем стиль по индексу
    style = SDXLStyle.get_by_index(style_index)
    
    config = SDXLConfig(auto_translate=True)
    client = SDXLClient(config)

    try:
        # Генерация изображения
        images = asyncio.run(client.generate(
            prompt=prompt,
            negative_prompt="",
            cfg_scale=7.5,
            style=style,
        ))
        image_url = images[0] if images else None
    except SDXLException as e:
        error_message = str(e)
        return render_template("error.html", error_message=error_message)
    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"
        return render_template("error.html", error_message=error_message)

    return render_template('index.html', image_url=image_url)

def run_flask():
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    run_flask()
