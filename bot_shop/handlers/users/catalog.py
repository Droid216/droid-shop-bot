from asgiref.sync import sync_to_async

from aiogram import types

from bot_shop.keyboards.inline.inline_catalog import ik_catalog, cb_category
from bot_shop.models import Category, Shop, Product
from create_bot import dp
from .start import bot_start


@dp.callback_query_handler(cb_category.filter())
async def clb_catalog(callback: types.CallbackQuery, callback_data: dict):
    try:
        list_objects = []
        parent = callback_data['id'] or None
        page = int(callback_data.get('page', 0))
        async for cat in Category.objects.filter(parent=parent).order_by('name').values():
            list_objects.append(cat)
        if not list_objects:
            async for item in Product.objects.filter(category=parent, in_stock=True).order_by('name').values():
                list_objects.append(item)
        shop_data = await sync_to_async(Shop.objects.first)()
        caption = shop_data.description
        image = str(shop_data.image)
        if parent is not None:
            cat_parent = await Category.objects.aget(pk=parent)
            caption = cat_parent.description or caption
            image = str(cat_parent.image) or image
        await callback.message.edit_media(media=types.InputMediaPhoto(media=types.InputFile('bot_shop/uploads/' + image),
                                                                      caption=caption),
                                          reply_markup=ik_catalog(list_objects, parent, page))
    except Exception:
        await callback.answer(text='Sorry category removed')
        await callback.message.delete()
        await bot_start(callback.message)

