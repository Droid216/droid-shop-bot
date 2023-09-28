from asgiref.sync import sync_to_async

from aiogram import types

from bot_shop.keyboards.inline.inline_buy import ik_buy
from bot_shop.keyboards.inline.inline_product import cb_buy
from bot_shop.models import Product, Shop
from create_bot import dp


@dp.callback_query_handler(cb_buy.filter())
async def clb_buy(callback: types.CallbackQuery, callback_data: dict):
    id_product = callback_data['id']
    product = await sync_to_async(Product.objects.filter(pk=id_product).first)()
    name_product = product.name
    shop_data = await sync_to_async(Shop.objects.first)()
    if shop_data.whatsapp:
        whatsapp_url = f"https://api.whatsapp.com/send?phone={shop_data.whatsapp}&text={shop_data.text_message} {name_product}"
    else:
        whatsapp_url = None
    telegram = bool(shop_data.telegram)
    phone = bool(shop_data.phone_number)
    await callback.message.edit_reply_markup(reply_markup=ik_buy(id_product=id_product,
                                                                 whatsapp=whatsapp_url,
                                                                 telegram=telegram,
                                                                 phone=phone))
