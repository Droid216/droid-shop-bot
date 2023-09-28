from asgiref.sync import sync_to_async

from aiogram import types

from bot_shop.models import Shop, Category
from create_bot import dp
from .catalog import clb_catalog
from .product import clb_product
from .start import bot_start
from bot_shop.keyboards.inline.inline_start import ik_start
from bot_shop.keyboards.inline.inline_catalog import cb_back
from bot_shop.keyboards.inline.inline_product import cb_back_category
from bot_shop.keyboards.inline.inline_buy import cb_back_product


@dp.callback_query_handler(text='back')
async def clb_back(callback: types.CallbackQuery):
    shop_data = await sync_to_async(Shop.objects.first)()
    text = shop_data.description
    contact = bool(shop_data.contact)
    await callback.message.edit_caption(caption=text,
                                        reply_markup=ik_start(contact))


@dp.callback_query_handler(cb_back.filter())
async def clb_back_cat(callback: types.CallbackQuery, callback_data: dict):
    try:
        parent = callback_data['id']
        cat_parent = await Category.objects.aget(pk=parent)
        callback_data['id'] = await sync_to_async(cat_parent.get_parent)()
        await clb_catalog(callback=callback, callback_data=callback_data)
    except Exception:
        await callback.answer(text='Sorry category removed')
        await callback.message.delete()
        await bot_start(callback.message)


@dp.callback_query_handler(cb_back_category.filter())
async def clb_back_prod(callback: types.CallbackQuery, callback_data: dict):
    await clb_catalog(callback=callback, callback_data=callback_data)


@dp.callback_query_handler(cb_back_product.filter())
async def clb_back_prod(callback: types.CallbackQuery, callback_data: dict):
    await clb_product(callback=callback, callback_data=callback_data)
