from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .inline_catalog import cb_category
from const_texts import *


def ik_contact() -> InlineKeyboardMarkup:
    ik = InlineKeyboardMarkup(row_width=1)
    ikb_catalog = InlineKeyboardButton(text=c_catalog, callback_data=cb_category.new(''))
    ikb_back = InlineKeyboardButton(text=c_back, callback_data='back')
    ik.add(ikb_catalog, ikb_back)
    return ik
