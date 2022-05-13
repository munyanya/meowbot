from aiogram import Dispatcher, types 
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StateGroup
from aiogram.dispatcher import FSMContext 
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import requests
import os
import texti *

class ByArcane(StatesGroup):
    waitingdata = State()

async def arcane1(message: types.Message):
    await.message.answer('Введите дату своего рождения')
    await state.update_data(data=message.text)

    user_data = await state.get_data()

