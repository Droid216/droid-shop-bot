from django.db import models
from django.conf import settings


class Shop(models.Model):
    name = models.CharField(max_length=50,
                            default="Your shop",
                            verbose_name='Name Shop')
    image = models.ImageField(upload_to='',
                              default=settings.DEFAULT_IMAGE,
                              verbose_name='Image')
    description = models.TextField(max_length=600,
                                   default="Hello!",
                                   verbose_name='Hello text')
    contact = models.TextField(max_length=600,
                               blank=True,
                               null=True,
                               verbose_name='Contact text')
    phone_number = models.CharField(max_length=20,
                                    blank=True,
                                    null=True,
                                    verbose_name='Phone number')
    whatsapp = models.CharField(max_length=20,
                                blank=True,
                                null=True,
                                help_text='The number must start with +',
                                verbose_name='WhatsApp number')
    telegram = models.CharField(max_length=65,
                                blank=True,
                                null=True,
                                verbose_name='Telegram username')
    text_message = models.TextField(max_length=200,
                                    blank=True,
                                    null=True,
                                    default="Hello, I would like to purchase the product",
                                    help_text="Beginning of a client's message",
                                    verbose_name='Client message')

    def save(self, *args, **kwargs):
        if Shop.objects.exists() and not self.pk:
            existing_record = Shop.objects.first()
            existing_record.name = self.name
            existing_record.photo_shop = self.image
            existing_record.hello_text = self.description
            existing_record.contact = self.contact
            existing_record.phone_number = self.phone_number
            existing_record.whatsapp = self.whatsapp
            existing_record.telegram = self.telegram
            existing_record.text_message = self.text_message
            existing_record.save()
            return existing_record
        else:
            return super(Shop, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shop'


try:
    if not Shop.objects.first():
        Shop().save()
except Exception:
    pass


class TelegramUser(models.Model):
    chat_id = models.CharField(max_length=20, primary_key=True, verbose_name='Telegram ID')
    first_name = models.CharField(max_length=64, verbose_name='First name')
    last_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='Last name')
    username = models.CharField(max_length=64, blank=True, null=True, verbose_name='Username Telegram')
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='Phone number')

    def __str__(self):
        return self.chat_id

    def get_user(self):
        return self.chat_id

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = 'Telegram user'
        verbose_name_plural = 'Telegram users'


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')
    parent = models.ForeignKey(to='self',
                               blank=True,
                               null=True,
                               on_delete=models.PROTECT,
                               verbose_name='Pre category')
    image = models.ImageField(upload_to='',
                              default=settings.DEFAULT_IMAGE,
                              verbose_name='Image')
    description = models.TextField(max_length=600,
                                   blank=True,
                                   null=True,
                                   verbose_name='Description')
    depth = models.TextField(default='', blank=True, null=True, verbose_name='Full catalog path')

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_parent(self):
        if self.parent:
            return self.parent.id
        return None

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')
    category = models.ForeignKey(to=Category,
                                 on_delete=models.PROTECT,
                                 verbose_name='Category')
    image = models.ImageField(upload_to='',
                              default=settings.DEFAULT_IMAGE,
                              verbose_name='Image')
    description = models.TextField(max_length=600,
                                   verbose_name='Description')
    in_stock = models.BooleanField(default=True, verbose_name='In stock')

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_category(self):
        return self.category.id

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
