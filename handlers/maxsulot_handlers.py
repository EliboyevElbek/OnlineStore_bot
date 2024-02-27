from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from Bot.store_bot.keyboards.inline_keyboards import (
    maxsulot_inline_keyboard,
    maxsulot_inline_edit_keyboard,
    maxsulot_inline_del_keyboard,
    maxsulot_inline_delete_keyboard,
)
from Bot.store_bot.states.maxsulot_states import MaxsulotState
from Bot.store_bot.config import DB_NAME
from Bot.store_bot.utils.databasa import Databasa

db = Databasa(DB_NAME)

maxsulot_router = Router()


@maxsulot_router.message(Command('maxsulotlar'))
async def maxsulotlar_handlers(message: Message):
    await message.answer(
        text='Barcha maxsulotlar',
        reply_markup=maxsulot_inline_keyboard()
    )


@maxsulot_router.message(Command('add_maxsulot'))
async def maxsulotlar_handlers(message: Message, state: FSMContext):
    await state.set_state(MaxsulotState.addMaxsulot)
    await message.answer("Yangi maxsulot nomini kiriting: ")

@maxsulot_router.message(MaxsulotState.addMaxsulot)
async def add_maxsulot(message: Message, state=FSMContext):
    # await state.update_data(maxsulot=message.text)
    if db.tekshiriuv(message.text):
        db.maxsulot_qosh(message.text)
        await message.answer("Maxsulot muvaffaqiyatli qo'shildi✅")
        await state.clear()
    else:
        await message.reply(f"{message.text}: maxsuloti mavjud❌")


@maxsulot_router.message(Command('edit_maxsulot'))
async def select_edit_maxsulot(message: Message, state: FSMContext):
    await state.set_state(MaxsulotState.startEditMaxsulot)
    await message.answer(
        text="O'zgartirmoqchi bo'lgan maxsulotingizni tanlang:",
        reply_markup=maxsulot_inline_edit_keyboard()
    )

@maxsulot_router.callback_query(MaxsulotState.startEditMaxsulot)
async def edit_maxsulot(callback: CallbackQuery, state:FSMContext):
    await state.set_state(MaxsulotState.finishEditMaxsulot)
    await state.update_data(edit_name=callback.data)
    await callback.message.edit_text("O'zgartirmoqchi bo'lgan nomingizni kiriting:")


@maxsulot_router.message(MaxsulotState.finishEditMaxsulot)
async def finish_edit_maxsulot(message: Message, state=FSMContext):
    if db.tekshiriuv(message.text):
        data = await state.get_data()
        if db.rename_maxsulot(eski_nomi=data.get('edit_name'), yangisi=message.text):
            await state.clear()
            await message.answer("Maxsulot nomi o'zgartirildi")
        else:
            await message.answer("Qandaydir xatolik❓")
    else:
        await message.answer(f"Boshqa nom tanlang --{message.text}-- nomi mavjud:")


@maxsulot_router.message(Command('delete_maxsulot'))
async def select_delete_maxsulot(message: Message, state: FSMContext):
    await state.set_state(MaxsulotState.startDeleteMaxsulot)
    await message.answer(
        text="Qaysi maxsulotni o'chirmoqchisiz:",
        reply_markup=maxsulot_inline_delete_keyboard()
    )

@maxsulot_router.callback_query(MaxsulotState.startDeleteMaxsulot)
async def del_maxsulot(callback: CallbackQuery, state=FSMContext):
    await state.set_state(MaxsulotState.finishDeleteMaxsulot)
    await state.update_data(nomi=callback.data)
    await callback.message.edit_text(
        text=f"Haqiqatdan ham {callback.data} maxsuloti o'chirilsinmi",
        reply_markup=maxsulot_inline_del_keyboard()
    )


@maxsulot_router.callback_query(MaxsulotState.finishDeleteMaxsulot)
async def finish_del_maxsulot(callback: CallbackQuery, state=FSMContext):
    if callback.data == 'yes':
        data = await state.get_data()
        if db.delete_maxsulot(nomi=data.get('nomi')):
            await callback.message.answer("Maxsulot o'chirildi")
            await callback.message.delete()
            await state.clear()
    else:
        await state.clear()
        await callback.message.answer("O'chirish bekor qilindi")
        await callback.message.delete()