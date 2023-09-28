from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .inline_catalog import cb_category
from const_texts import *


def ik_start(contact: False) -> InlineKeyboardMarkup:
    ik = InlineKeyboardMarkup(row_width=1)
    ikb_catalog = InlineKeyboardButton(text=c_catalog, callback_data=cb_category.new(''))
    ikb_contact = InlineKeyboardButton(text=c_contact, callback_data='contact')
    ik.add(ikb_catalog)
    if contact:
        ik.add(ikb_contact)
    return ik
