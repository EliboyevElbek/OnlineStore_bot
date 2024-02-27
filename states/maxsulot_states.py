from aiogram.fsm.state import State, StatesGroup

class MaxsulotState(StatesGroup):
    addMaxsulot = State()

    startEditMaxsulot = State()
    finishEditMaxsulot = State()

    startDeleteMaxsulot = State()
    finishDeleteMaxsulot = State()

class ProductState(StatesGroup):
    addProduct = State()
    addProductName = State()
    addProductImage = State()

    startDeleteProduct = State()

