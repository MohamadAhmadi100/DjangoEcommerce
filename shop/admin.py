from django.contrib import admin
from .models import Category, Product, Picture


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'inventory')
    list_filter = ('inventory', 'created')
    list_editable = ('inventory', 'price')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('category',)
    actions = ('zero_inventory', 'plus_fifty', 'minus_fifty')

    def zero_inventory(self, request, queryset):
        rows = queryset.update(inventory=0)
        self.message_user(request, f"موجودی {rows} محصول صفر شد")

    zero_inventory.short_description = 'تغییر موجودی محصول به صفر'

    def plus_fifty(self, request, queryset):
        for query in queryset:
            query.inventory += 50
            query.save()
        rows = queryset.count()
        self.message_user(request, f"موجودی {rows} محصول پنجاه عدد اضافه شد")

    plus_fifty.short_description = 'افزایش 50 عدد موجودی محصول'

    def minus_fifty(self, request, queryset):
        for query in queryset:
            query.inventory -= 50
            query.save()
        rows = queryset.count()
        self.message_user(request, f"موجودی {rows} محصول پنجاه عدد کم شد")

    minus_fifty.short_description = 'کاهش 50 عدد موجودی محصول'


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('album', 'id', 'default')
    list_filter = ('default',)
    list_editable = ('default',)
