from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import  types

from .router import router
from core.checksubscribe.checker import subscription_required


@router.message(Command("start"))
@subscription_required
async def start_command(message: types.Message):
    """Приветствует пользователя и предлагает начать."""
    await message.reply(
        "Привет! Я бот для отслеживания питания. Используй /add_food, чтобы добавить запись о еде, /show_today, чтобы увидеть записи за сегодня, и /help для справки."
    )


@router.message(Command("help"))
@subscription_required
async def help_command(message: types.Message):
    """Предоставляет информацию о командах бота."""
    await message.reply(
        "Вот список доступных команд:\n"
        "/start - Начать работу с ботом\n"
        "/add_food - Добавить запись о приеме пищи\n"
        "/show_today - Показать записи о еде за сегодня\n"
        "/help - Получить справку\n"
        "/register - добавить свои данные"
    )