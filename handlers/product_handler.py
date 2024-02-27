from aiogram import Router
from aiogram.filters import Command, state
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from Bot.store_bot.keyboards.inline_keyboards import maxsulot_inline_edit_keyboard, product_inline_delete_keyboard
from Bot.store_bot.states.maxsulot_states import ProductState
from Bot.store_bot.utils.databasa import Databasa
from Bot.store_bot.config import DB_NAME

db = Databasa(DB_NAME)

product_router = Router()

@product_router.message(Command('add_product'))
async def select_add_product(message: Message, state: FSMContext):
    await state.set_state(ProductState.addProduct)
    await message.answer(
        text="Qaysi turdanligini tanlang",
        reply_markup=maxsulot_inline_edit_keyboard()
    )

@product_router.callback_query(ProductState.addProduct)
async def add_product(callback: CallbackQuery, state:FSMContext):
    await state.set_state(ProductState.addProductName)
    await callback.message.answer("Product Nomi:")
    await callback.message.delete()


@product_router.message(ProductState.addProductName)
async def add_name(message: Message, state: FSMContext):
    await state.set_state(ProductState.addProductImage)
    await state.update_data(product_name=message.text)
    await message.answer("Rasm yuboring: ")


@product_router.message(ProductState.addProductImage)
async def add_name(message: Message, state: FSMContext):
    if message.photo:
        await state.set_state(ProductState.addProductImage)
        await state.update_data(product_image=message.photo[-1].file_id)
        all_data = await state.get_data()
        if db.add_product(all_data.get('product_name'), all_data.get('product_image')):
            await message.answer("Product joylandi:")
            await state.clear()
    else:
        await message.reply("Faqat rasm yuboring:")

@product_router.message(Command('delete_product'))
async def start_delete_product(message: Message, state:FSMContext):
    await state.set_state(ProductState.startDeleteProduct)
    await message.answer(
        text="O'chirmoqchi bo'lgan productni tanlangg",
        reply_markup=product_inline_delete_keyboard()
    )

@product_router.callback_query(ProductState.startDeleteProduct)
async def del_product(query: CallbackQuery, state: FSMContext):
    await state.update_data(nomi=query.data)
    await state.set_state() #oxiriga yetmagan

@product_router.message(Command('all_product'))
async def all_product(message: Message):
    products = db.all_product()
    for product in products:
        await message.answer_photo(
            photo=product[2],
            caption=f"<b>{product[1]}</b>"
        )



