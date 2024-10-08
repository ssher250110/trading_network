from django.contrib import admin

from trade.models import LinkNetwork, ContactData, Product


@admin.action(description="Reset debt")
def delete_debt(modeladmin, request, queryset):
    """Функция для обнуления задолженности перед поставщиком"""
    queryset.update(debt=0)


@admin.register(ContactData)
class ContactDataAdmin(admin.ModelAdmin):
    """Отображение информации о контактных данных"""

    list_display = ["id", "email", "country", "city", "street", "house_number", "creator"]
    list_filter = ["email", "country"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Отображение информации о продукте"""

    list_display = ["name_product", "model_product", "product_release_date", "creator"]
    list_filter = ["name_product"]


@admin.register(LinkNetwork)
class LinkNetworkAdmin(admin.ModelAdmin):
    """Отображение информации о звене цепи"""

    list_display = ["name", "contact", "product", "level", "provider", "debt", "created_at", "creator"]
    list_filter = ["name"]
    actions = [delete_debt]
