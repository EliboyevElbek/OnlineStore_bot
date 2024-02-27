from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Bot.store_bot.config import DB_NAME
from Bot.store_bot.utils.databasa import Databasa

db = Databasa(DB_NAME)


def maxsulot_inline_keyboard():
    maxsulotlar = db.get_maxsulotlar()
    rows = []
    for maxsulot in maxsulotlar:
        rows.append([
            InlineKeyboardButton(text=maxsulot[1], callback_data=str(maxsulot[0]))
        ])

    in_kb = InlineKeyboardMarkup(
        inline_keyboard=rows
    )

    return in_kb


def maxsulot_inline_edit_keyboard():
    maxsulotlar = db.get_maxsulotlar()
    rows = []
    for maxsulot in maxsulotlar:
        rows.append([
            InlineKeyboardButton(text=maxsulot[1], callback_data=str(maxsulot[1]))
        ])

    in_edit_kb = InlineKeyboardMarkup(
        inline_keyboard=rows
    )

    return in_edit_kb


def maxsulot_inline_delete_keyboard():
    maxsulotlar = db.get_maxsulotlar()
    rows = []
    for maxsulot in maxsulotlar:
        rows.append([
            InlineKeyboardButton(text=maxsulot[1], callback_data=str(maxsulot[1]))
        ])

    in_del_kb = InlineKeyboardMarkup(
        inline_keyboard=rows
    )

    return in_del_kb


def maxsulot_inline_del_keyboard():
    rows = [
        InlineKeyboardButton(text='HA', callback_data='yes'),
        InlineKeyboardButton(text='YO\'Q', callback_data='no')
    ]

    in_del_kb = InlineKeyboardMarkup(
        inline_keyboard=[rows]
    )

    return in_del_kb

def product_inline_delete_keyboard():
    products = db.get_product()
    rows = []
    for product in products:
        rows.append([
            InlineKeyboardButton(text=product[1], callback_data=str(product[1]))
        ])

    prod_in_del_kb = InlineKeyboardMarkup(
        inline_keyboard=rows
    )

    return prod_in_del_kb

