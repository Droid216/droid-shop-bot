from asgiref.sync import sync_to_async

from aiogram import types

from bot_shop.keyboards.inline.inline_contact import ik_contact
from bot_shop.models import Shop
from create_bot import dp


@dp.callback_query_handler(text='contact')
async def clb_contact(callback: types.CallbackQuery):
    shop_data = await sync_to_async(Shop.objects.first)()
    contact = shop_data.contact
    await callback.message.edit_caption(caption=contact,
                                        reply_markup=ik_contact())
