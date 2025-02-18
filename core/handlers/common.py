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
"""Привет! 👋

Для доступа ко всем функциям бота [Название вашего бота] необходимо:
1.  Зарегистрироваться.
2.  Оплатить подписку.

/register для начала регистрации

Полный функционал откроется после оплаты.""")


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
        "/register - добавить свои данные\n"
    )