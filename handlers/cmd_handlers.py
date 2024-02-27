from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from Bot.store_bot.config import admins
from Bot.store_bot.utils.admin_command import admin_commands, users_commands

cmd_router = Router()


@cmd_router.message(CommandStart())
async def start_handler(message: Message):
    if message.from_user.id in admins:
        await message.bot.set_my_commands(commands=admin_commands)
        await message.answer("Xush kelibsiz, ADMIN!")

    else:
        await message.bot.set_my_commands(commands=users_commands)
        await message.answer("Xush kelibsiz")
