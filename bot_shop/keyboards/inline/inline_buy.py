from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from const_texts import *

cb_back_product = CallbackData('back_product', 'id')
cb_call_manager = CallbackData('call_manager', 'action')


def ik_buy(id_product, whatsapp, telegram, phone=None) -> InlineKeyboardMarkup:
    ik = InlineKeyboardMarkup()
    if whatsapp:
        ikb_whatsapp = InlineKeyboardButton(text=c_whatsapp,
                                            url=whatsapp)
        ik.add(ikb_whatsapp)
    if telegram:
        ikb_telegram = InlineKeyboardButton(text=c_telegram, callback_data=cb_call_manager.new('telegram'))
        ik.add(ikb_telegram)
    if phone:
        ik_phone = InlineKeyboardButton(text=c_phone, callback_data=cb_call_manager.new('phone'))
        ik.add(ik_phone)
    ikb_back = InlineKeyboardButton(text=c_back, callback_data=cb_back_product.new(id_product))
    ik.add(ikb_back)
    return ik
