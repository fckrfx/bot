'''
keyboards live here
'''

from aiogram.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup,
                           KeyboardButton,
                           ReplyKeyboardMarkup,
                           ReplyKeyboardRemove
                           )


rm = ReplyKeyboardRemove()


rk01 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Menu')],
                                     [KeyboardButton(text='SignUp'),
                                      KeyboardButton(text='About')]],
                           resize_keyboard=True,
                           one_time_keyboard=True,
                           input_field_placeholder='PUSH THE BUTT0N',
                           )


rk02 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='share contact',
                                                     request_contact=True)]],
                           resize_keyboard=True,
                           one_time_keyboard=True,
                           input_field_placeholder='SHARE CONTACT',
                           )


ik01 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='ibut00', callback_data='ibut00')],
    [InlineKeyboardButton(text='ibut01', callback_data='ibut01'),
     InlineKeyboardButton(text='ibut10', callback_data='ibut10')]])
