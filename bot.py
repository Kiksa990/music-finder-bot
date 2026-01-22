import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from config import API_TOKEN
import analyzer
import downloader

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def start(message: types.Message):
    nickname = message.from_user.first_name or message.from_user.username or "юзер"

    welcome_text = (
        f"👋 Добро пожаловать, {nickname}!\n\n"
        "Ты попал в бота, который умеет находить музыку и скачивать видео 🎶📽️.\n"
        "Просто пришли ссылку на видео — и я помогу тебе его скачать.\n"
        "А если загрузишь аудио, я постараюсь определить, что это за трек 🔍."
    )

    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="📽️ Скачать видео", callback_data="download"),
                types.InlineKeyboardButton(text="🎧 Найти музыку", callback_data="music")
            ]
        ]
    )
    await message.answer(welcome_text, reply_markup=keyboard)

# Обработка кнопки "Скачать видео"
@dp.callback_query(lambda c: c.data == "download")
async def process_download(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Отправь мне ссылку на видео 🎬")

# Обработка кнопки "Найти музыку"
@dp.callback_query(lambda c: c.data == "music")
async def process_music(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Отправь мне аудио 🎧")

# Обработка ссылок
@dp.message(lambda message: message.text and message.text.startswith("http"))
async def handle_url(message: types.Message):
    if "youtube.com" in message.text or "youtu.be" in message.text:
        await message.answer("⏳ Скачиваю видео, подожди немного...")
        result = downloader.download_video(message.text)
        await message.answer(result, parse_mode="Markdown")
    else:
        await message.answer("Ссылка получена, но пока поддерживаю только YouTube.")

# Обработка аудио
@dp.message(F.audio)
async def handle_audio(message: types.Message):
    file_id = message.audio.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    audio_url = f"https://api.telegram.org/file/bot{API_TOKEN}/{file_path}"

    await message.answer("🎶 Распознаю музыку...")
    result = analyzer.recognize_music(audio_url)
    await message.answer(f"Результат: {result}")

async def main():
    print("✅ Music Finder запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())