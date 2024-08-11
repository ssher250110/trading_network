from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Отображение информации о пользователях в админ панели"""

    list_display = [
        "id",
        "email",
        "last_name",
        "first_name",
        "middle_name",
        "phone",
        "role",
        "is_active",
        "last_login",
    ]
    search_fields = ["email", "last_name", "first_name", "last_login"]
    list_filter = ["role", "is_active"]
    ordering = ["email"]
