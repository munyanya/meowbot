from aiogram import Dispatcher, types 
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#async def echo(message: types.Message):
    #print(message)
    #await message.answer(message.text)

async def menu(message: types.Message):
    #meny_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    #b1 = KeyboardButton(text='котик')
    #b2 = KeyboardButton(text='кися')
    #b3 = KeyboardButton(text='кося')

    #menu_kb.add(b1, b2, b3)
    #await message.answer('Main.menu', reply_markup=menu_kb)

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

async def b3(message: types.Message):
    message.answer('Нажал на косю')
async def b2(message: types.Message):
    message.answer('Нажал на кисю')
async def b1(message: types.Message):
    message.answer('Нажал на котика')

def register_common_hadlers(dp: Dispatcher):
    dp.register_message_handler(menu, commands = 'menu', state='*')
    dp.register_message_handler(b3, Text(equals='кося', ignore_case=True))
    dp.register_message_handler(b2, Text(equals='кися', ignore_case=True))
    dp.register_message_handler(b1, Text(equals='котик', ignore_case=True))
    # dp.register_message_handler(echo, content_types= types.message.ContentType.TEXT)
    dp.register_callback_query_handler(callback_handler)