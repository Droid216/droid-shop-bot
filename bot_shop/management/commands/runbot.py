from django.core.management.base import BaseCommand

from aiogram import executor

from bot_shop.handlers import *
from create_bot import dp


async def on_startup(_):
    print('Start!')


class Command(BaseCommand):
    help = 'RUN COMMAND: python manage.py runbot'

    def handle(self, *args, **options):
        executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
