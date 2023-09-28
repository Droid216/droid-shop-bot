from asgiref.sync import sync_to_async

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from bot_shop.models import TelegramUser, Shop
from create_bot import dp
from bot_shop.keyboards.inline.inline_start import ik_start


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = await sync_to_async(TelegramUser.objects.filter(pk=message.from_user.id).exists)()
    if user:
        await sync_to_async(TelegramUser.objects.filter(
            pk=message.from_user.id).update)(first_name=message.from_user.first_name,
                                             last_name=message.from_user.last_name,
                                             username=message.from_user.username)
    else:
        await sync_to_async(TelegramUser.objects.create)(chat_id=message.from_user.id,
                                                         first_name=message.from_user.first_name,
                                                         last_name=message.from_user.last_name,
                                                         username=message.from_user.username)

    shop_data = await sync_to_async(Shop.objects.first)()
    text = shop_data.description
    image = str(shop_data.image)
    contact = bool(shop_data.contact)
    await message.answer_photo(photo=types.InputFile('bot_shop/uploads/' + image),
                               caption=text,
                               reply_markup=ik_start(contact))
