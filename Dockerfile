# Базовый образ Python
FROM python:3.11-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Скопировать список зависимостей
COPY requirements.txt .

# Установить зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопировать весь проект
COPY . .

# Запуск бота
CMD ["python", "bot.py"]