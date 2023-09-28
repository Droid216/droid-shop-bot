from asgiref.sync import sync_to_async

from aiogram import types

from bot_shop.keyboards.inline.inline_buy import cb_call_manager
from bot_shop.models import Shop
from create_bot import dp
from const_texts import *


@dp.callback_query_handler(cb_call_manager.filter())
async def clb_call_manager(callback: types.CallbackQuery, callback_data: dict):
    await callback.answer()
    shop_data = await sync_to_async(Shop.objects.first)()
    if callback_data['action'] == 'telegram' and shop_data.telegram:
        username = shop_data.telegram.replace('@', '')
        await callback.message.answer(text=f'{c_call_manager} [{username}](https://telegram.me/{username})',
                                      disable_web_page_preview=True,
                                      parse_mode=types.ParseMode.MARKDOWN_V2)
    elif callback_data['action'] == 'phone' and shop_data.phone_number:
        await callback.message.answer(text=f'{c_call_manager} `{shop_data.phone_number}`',
                                      parse_mode=types.ParseMode.MARKDOWN_V2)
    else:
        await callback.message.answer(text=c_call_sorry)
