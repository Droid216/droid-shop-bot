from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from const_texts import *

cb_back_category = CallbackData('back_category', 'id')
cb_buy = CallbackData('buy', 'id')


def ik_product(product, category) -> InlineKeyboardMarkup:
    ik = InlineKeyboardMarkup()
    ikb_buy = InlineKeyboardButton(text=c_buy, callback_data=cb_buy.new(product))
    ikb_back = InlineKeyboardButton(text=c_back, callback_data=cb_back_category.new(category))
    ik.add(ikb_buy).add(ikb_back)
    return ik
