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

2. Enter the image description in the text field

3. Select the desired style from the dropdown menu

4. Click the "Generate" button

5. Wait for the image generation to complete (may take a few seconds)

### Available Styles
- (No style) - No style
- Cinematic - Cinematic
- Photographic - Photographic
- Anime - Anime
- Manga - Manga
- Digital Art - Digital Art
- Pixel art - Pixel art
- Fantasy art - Fantasy art
- Neonpunk - Neonpunk
- 3D Model - 3D Model

## Requirements
- Python 3.7+

- Stable internet connection

- Web browser with JavaScript support



# Русская инструкция


# SDXL Image Generator

Веб-приложение для генерации изображений с помощью модели SDXL через WebSocket соединение.

## Функциональность

- Генерация изображений по текстовому описанию (prompt)
- Выбор стиля изображения из 10 доступных вариантов
- Автоматический перевод с русского на английский
- Простой и интуитивно понятный веб-интерфейс

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/ArtemProgrammerIT/AI-Image.git
cd AI-Image
```
### 2.Создание виртуального окружения (рекомендуется)

```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
# или
venv\Scripts\activate  # для Windows
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Запуск приложения

```bash
python app.py
```
Приложение будет доступно по адресу: http://127.0.0.1:5000 ___(Либо по вашему лично сгенерированому url)___

### Использование
1. Откройте веб-браузер и перейдите по [адресу](http://127.0.0.1:5000)

2. Введите описание изображения в текстовое поле

3. Выберите желаемый стиль из выпадающего списка

4. Нажмите кнопку "Сгенерировать"

5. Дождитесь завершения генерации изображения (может занять несколько секунд)

### Доступные стили
- (No style) - Без стиля
- Cinematic - Кинематографический
- Photographic - Фотографический
- Anime - Аниме
- Manga - Манга
- Digital Art - Цифровое искусство
- Pixel art - Пиксель-арт
- Fantasy art - Фэнтези
- Neonpunk - Неонпанк
- 3D Model - 3D модель


## Требования
- Python 3.7+

- Стабильное интернет-соединение

- Веб-браузер с поддержкой JavaScript
