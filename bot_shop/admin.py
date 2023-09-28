from django.contrib import admin

from .models import Shop, TelegramUser, Category, Product


class ShopAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "chat_id", 'username']
    search_fields = ["first_name", "last_name", "chat_id", 'username']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["get_name", "parent", "depth"]
    search_fields = ["name", "depth"]
    ordering = ["depth"]
    readonly_fields = ["depth"]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent":
            categories_with_products = Product.objects.values_list('category_id', flat=True)
            kwargs["queryset"] = Category.objects.exclude(pk=request.resolver_match.kwargs.get('object_id')).\
                exclude(pk__in=categories_with_products).order_by('depth')
            print(kwargs["queryset"])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.save()
        for category in Category.objects.all():
            list_parent = [category.name]
            cat = category.parent
            while cat:
                list_parent.append(cat.name)
                cat = cat.parent
            category.depth = ' >> '.join(list_parent[::-1])
            category.save()

    def get_name(self, obj):
        name = ' ' + obj.name
        cat = obj.parent
        while cat:
            name = '>' + name
            cat = cat.parent
        return name

    get_name.short_description = "Category"
    get_name.admin_order_field = "name"


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    ordering = ['category', 'name']
    search_fields = ['name', 'category__name']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            categories = Category.objects.values_list('parent_id', flat=True)
            kwargs["queryset"] = Category.objects.exclude(pk__in=list(categories)).order_by('name')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Shop, ShopAdmin)
admin.site.register(TelegramUser, TelegramUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
