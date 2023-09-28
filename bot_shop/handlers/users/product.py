from asgiref.sync import sync_to_async

from aiogram import types

from .start import bot_start
from bot_shop.keyboards.inline.inline_catalog import cb_product
from bot_shop.keyboards.inline.inline_product import ik_product
from bot_shop.models import Shop, Product
from create_bot import dp


@dp.callback_query_handler(cb_product.filter())
async def clb_product(callback: types.CallbackQuery, callback_data: dict):
    try:
        id_product = callback_data['id']
        product = await Product.objects.aget(pk=id_product)
        category = await sync_to_async(product.get_category)()
        caption = product.description
        shop_data = await sync_to_async(Shop.objects.first)()
        image = str(product.image) or str(shop_data.image)
        await callback.message.edit_media(media=types.InputMediaPhoto(media=types.InputFile('bot_shop/uploads/' + image),
                                                                      caption=caption),
                                          reply_markup=ik_product(product.id, category))
    except Exception:
        await callback.answer(text='Sorry product removed')
        await callback.message.delete()
        await bot_start(callback.message)

