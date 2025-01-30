# телеграм бот для уведомления о заявке
# bot = telebot.TeleBot('7240126305:AAE1xAe53NivxVY8gInrMmfDjDx_G0iod_s')
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_ADMIN_ID

# Токен бота, полученный от BotFather


# Создаем объект бота и диспетчера
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# Глобальная переменная для хранения ID пользователя
USER_ID = TELEGRAM_ADMIN_ID

async def send_message(body):
    """
    Функция отправки сообщения конкретному пользователю.
    """
    global USER_ID
    if not USER_ID:
        print("USER_ID не установлен. Сначала отправь команду /start в боте, чтобы получить ID.")
        return

    title = "🔔Новая заявка"
    text = '👤 От:' + body
    url = "https://example.com"

     # Создаём клавиатуру с кнопкой
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Открыть по ссылке", url=url)]
    ])

    # Отправляем сообщение пользователю
    await bot.send_message(USER_ID, f"<b>{title}</b>\n\n{text}", parse_mode="HTML", reply_markup=keyboard)


async def main():
    """
    Основная функция, запускающая бота.
    """
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)