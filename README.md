# SDXL Image Generator

A web application for generating images using the SDXL model via WebSocket connection.

## Functionality

- Image generation based on text descriptions (prompts)
- Selection of image styles from 10 available options
- Automatic translation from Russian to English
- Simple and intuitive web interface

## Installation and Running

### 1. Cloning the Repository

```bash
git clone https://github.com/ArtemProgrammerIT/AI-Image.git
cd AI-Image
```

### 2. Creating a Virtual Environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # for Linux/Mac
# or
venv\Scripts\activate  # for Windows
```

### 3. Installing Dependencies

```bash
pip install -r requirements.txt
```

### 4. Running the Application

```bash
python app.py
```
The application will be available at: http://127.0.0.1:5000 ___(Or at your personally generated URL)___

### Usage
1. Open a web browser and go to [this address](http://127.0.0.1:5000)

2. Enter the image description on English/Russian in the text field

3. Select the desired style from the dropdown menu

4. Click the "Generate" button

5. Wait for the image generation to complete (may take a few seconds)

### Available Styles
- (No style)
- Cinematic
- Photographic
- Anime
- Manga
- Digital Art
- Pixel art
- Fantasy art
- Neonpunk
- 3D Model


# Main Points for Creating a Prompt

1. **Image Theme**:
   - Define the main theme (e.g., cityscape, nature, portrait).

2. **Stylistics**:
   - Specify the desired style (realism, abstraction, minimalism, etc.).

3. **Color Palette**:
   - Determine the main colors or mood (bright, pastel, contrasting).

4. **Composition**:
   - Describe the arrangement of objects (central element, background, details).

5. **Emotions and Atmosphere**:
   - Indicate what feelings the image should evoke (joy, calmness, nostalgia).

6. **Additional Elements**:
   - Specify particular details or objects to be included (e.g., buildings, people, nature).

7. **Format and Size**:
   - Define the desired format (portrait, landscape) and size of the image.

####Example: The image depicts Central Park in the heart of New York City, where green pathways and well-kept lawns contrast with the surrounding skyscrapers. People are enjoying nature, walking or riding bicycles, creating an atmosphere of tranquility amidst the bustling urban environment.


### Requirements
- Python 3.7+

- Stable internet connection

- Web browser with JavaScript support

