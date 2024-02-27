from aiogram.types import BotCommand



admin_commands = [
    BotCommand(command='start', description='Botni ishga tushirish'),
    BotCommand(command='maxsulotlar', description='Barcha maxsulotlarni korish'),
    BotCommand(command='add_maxsulot', description='Maxsulot qo\'shish'),
    BotCommand(command='edit_maxsulot', description='Maxsulot nomini o\'zgartirish'),
    BotCommand(command='delete_maxsulot', description='Maxsulotni o\'chirish'),
    BotCommand(command='add_product', description='Tovar qo\'shish'),
    BotCommand(command='delete_product', description='Tovarni o\'chirish'),
    BotCommand(command='all_product', description='Barcha tovarlar'),
]

users_commands = [
    BotCommand(command='start', description='Botni ishga tushirish'),
    BotCommand(command='help', description='Bot haqida ma\'lumot olish'),
]