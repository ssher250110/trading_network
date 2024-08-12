from django.contrib import admin

from trade.models import LinkNetwork


@admin.action(description="Reset debt")
def delete_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(LinkNetwork)
class LinkNetworkAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "email",
        "country",
        "city",
        "street",
        "house_number",
        "name_product",
        "model_product",
        "product_release_date",
        "provider",
        "debt",
        "created_at",
        "level",
        "owner",
    ]
    list_filter = ["city"]
    actions = [delete_debt]
