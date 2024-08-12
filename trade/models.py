from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

NULLABLE = {"null": True, "blank": True}


class LinkNetwork(models.Model):
    class Level(models.IntegerChoices):
        FACTORY = 0, _("Завод")
        RETAIL_NETWORK = 1, _("Розничная сеть")
        INDIVIDUAL_BUSINESSMAN = 2, _("Индивидуальный предприниматель")

    name = models.CharField(
        max_length=255, verbose_name="Название звена сети", help_text="Укажите название звена сети"
    )
    email = models.EmailField(verbose_name="Почта", help_text="Укажите электронную почту")
    country = models.CharField(max_length=255, verbose_name="Название страны", help_text="Укажите название страны")
    city = models.CharField(max_length=255, verbose_name="Название города", help_text="Укажите название города")
    street = models.CharField(max_length=255, verbose_name="Название улицы", help_text="Укажите название улицы")
    house_number = models.PositiveSmallIntegerField(verbose_name="Номер дома", help_text="Укажите номер дома")
    name_product = models.CharField(
        max_length=255, verbose_name="Название продукта", help_text="Укажите название продукта"
    )
    model_product = models.CharField(
        max_length=255, verbose_name="Модель продукта", help_text="Укажите модель продукта"
    )
    product_release_date = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата выхода продукта на рынок",
        help_text="Укажите дату выхода продукта на рынок",
    )
    level = models.PositiveSmallIntegerField(
        choices=Level, verbose_name="Уровень звена сети", help_text="Укажите уровень звена сети"
    )
    provider = models.ForeignKey(
        "self", on_delete=models.SET_NULL, **NULLABLE, verbose_name="Поставщик", help_text="Укажите поставщика"
    )
    debt = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Задолженность перед поставщиком",
        help_text="Укажите задолженность перед поставщиком",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания звена сети")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь, добавивший звено сети",
        help_text="Укажите пользователя, добавившего звено сети",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"
