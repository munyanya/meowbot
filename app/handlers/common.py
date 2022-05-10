from aiogram import Dispatcher, types 
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from texti import *

#async def echo(message: types.Message):
    #print(message)
    #await message.answer(message.text)

async def menu(message: types.Message):
    menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    v1 = KeyboardButton(text='котик')
    v2 = KeyboardButton(text='кися')
    v3 = KeyboardButton(text='кося')

    menu_kb.add(v1, v2, v3)
    await message.answer('Main.menu', reply_markup=menu_kb)

    inline_menu_kb = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton(text='мяу', callback_data='callback1', url = "https://astrafarm.com/images/encyclopedia/ittenVes170221.jpg")
    b2 = InlineKeyboardButton(text='мур', callback_data='callback2')
    b3 = InlineKeyboardButton(text='мыр', callback_data='callback3')
    inline_menu_kb.add(b1, b2, b3)
    await message.answer('Main menu', reply_markup=inline_menu_kb)

async def callback_handler(message: types.Message):
    if message.data == 'callback1':
        await message.answer('meow 1')
    if message.data == 'callback2':
        await message.answer('meow 2')
    if message.data == 'callback3':
        await message.answer('meow 3')    

async def v3(message: types.Message):
    await message.answer_photo('https://funart.pro/uploads/posts/2021-04/1618251508_38-p-samie-milie-koti-zhivotnie-krasivo-foto-41.jpg')
    await message.answer('На тебя похож')
async def v2(message: types.Message):
    await message.answer_photo('https://99px.ru/sstorage/56/2011/11/image_560211111550212386889.jpg')
    await message.answer('На тебя на похож')
async def v1(message: types.Message):
    await message.answer(poznanie)

def register_common_hadlers(dp: Dispatcher):
    dp.register_message_handler(menu, commands = 'menu', state='*')
    dp.register_message_handler(v3, Text(equals='кося', ignore_case=True))
    dp.register_message_handler(v2, Text(equals='кися', ignore_case=True))
    dp.register_message_handler(v1, Text(equals='котик', ignore_case=True))
    # dp.register_message_handler(echo, content_types= types.message.ContentType.TEXT)
    dp.register_callback_query_handler(callback_handler)