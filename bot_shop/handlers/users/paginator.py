from aiogram import types

from bot_shop.handlers.users.catalog import clb_catalog
from bot_shop.keyboards.inline.inline_catalog import cb_page
from create_bot import dp


@dp.callback_query_handler(cb_page.filter())
async def clb_page(callback: types.CallbackQuery, callback_data: dict):
    await clb_catalog(callback=callback, callback_data=callback_data)
