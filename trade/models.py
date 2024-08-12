from django.conf import settings
from django.db import models
from django.utils import timezone

NULLABLE = {"null": True, "blank": True}


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название продукта", help_text="Укажите название продукта")
    model = models.CharField(max_length=255, verbose_name="Модель продукта", help_text="Укажите модель продукта")
    product_release_date = models.DateTimeField(
        default=timezone.now(),
        verbose_name="Дата выхода продукта на рынок",
        help_text="Укажите дату выхода продукта на рынок",
    )
    added_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь, добавивший продукт",
        help_text="Укажите пользователя, добавившего продукт",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
