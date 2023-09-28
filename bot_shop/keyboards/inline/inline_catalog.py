from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from const_texts import *


cb_category = CallbackData('catalog', 'id')
cb_product = CallbackData('product', 'id')
cb_back = CallbackData('back', 'id')
cb_page = CallbackData('page', 'id', 'page')


def ik_catalog(list_object, parent, page=0) -> InlineKeyboardMarkup:
    ik = InlineKeyboardMarkup()
    parent = parent or ''
    len_list = len(list_object)
    count_object = 8
    if len_list > count_object:
        if len_list > (page + 1) * count_object:
            list_object = list_object[count_object * page:count_object * (page + 1)]
        else:
            list_object = list_object[count_object * page:]

    for obj in list_object:
        if obj.get('category_id', False):
            ikb = InlineKeyboardButton(text=obj['name'], callback_data=cb_product.new(obj['id']))
        else:
            ikb = InlineKeyboardButton(text=obj['name'], callback_data=cb_category.new(obj['id']))
        ik.add(ikb)

    if len_list > count_object:
        max_page = (len_list // count_object) - 1 if (len_list % count_object) == 0 else (len_list // count_object)
        prev_page = max_page if page == 0 else page - 1
        next_page = 0 if page == max_page else page + 1
        ikb_prev = InlineKeyboardButton(text=c_prev, callback_data=cb_page.new(parent, prev_page))
        ikb_next = InlineKeyboardButton(text=c_next, callback_data=cb_page.new(parent, next_page))
        ik.add(ikb_prev, ikb_next)

    if parent:
        ikb_back = InlineKeyboardButton(text=c_back, callback_data=cb_back.new(parent))
    else:
        ikb_back = InlineKeyboardButton(text=c_back, callback_data='back')
    ik.add(ikb_back)
    return ik
