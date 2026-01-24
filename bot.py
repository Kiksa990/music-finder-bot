from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import scanner
import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# Меню сканера
scanner_menu = InlineKeyboardMarkup(row_width=2)
scanner_menu.add(
    InlineKeyboardButton("Lite+Deep", callback_data="scan_lite"),
    InlineKeyboardButton("Deep Scan", callback_data="scan_deep"),
    InlineKeyboardButton("Basic Defense", callback_data="scan_basic"),
    InlineKeyboardButton("Pro Shield", callback_data="scan_pro")
)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Выберите режим сканера:", reply_markup=scanner_menu)

@dp.callback_query_handler(lambda c: c.data.startswith("scan_"))
async def process_scan(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    mode = callback_query.data

    # Для примера — проверяем тестовый файл
    file_path = "test.txt"

    if mode == "scan_lite":
        result = scanner.scan_lite(user_id, file_path)
    elif mode == "scan_deep":
        result = scanner.scan_deep(user_id, file_path)
    elif mode == "scan_basic":
        result = scanner.scan_basic(user_id, file_path)
    elif mode == "scan_pro":
        result = scanner.scan_pro(user_id, file_path)
    else:
        result = "❌ Неизвестный режим."

    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(user_id, result)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)