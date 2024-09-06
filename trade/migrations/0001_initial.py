# Generated by Django 5.1 on 2024-09-06 09:50

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactData",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "email",
                    models.EmailField(help_text="Укажите электронную почту", max_length=254, verbose_name="Почта"),
                ),
                (
                    "country",
                    models.CharField(
                        help_text="Укажите название страны", max_length=255, verbose_name="Название страны"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        help_text="Укажите название города", max_length=255, verbose_name="Название города"
                    ),
                ),
                (
                    "street",
                    models.CharField(
                        help_text="Укажите название улицы", max_length=255, verbose_name="Название улицы"
                    ),
                ),
                (
                    "house_number",
                    models.PositiveSmallIntegerField(help_text="Укажите номер дома", verbose_name="Номер дома"),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите пользователя, добавившего контактные данные",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь, добавивший контактные данные",
                    ),
                ),
            ],
            options={
                "verbose_name": "Контактные данные",
                "verbose_name_plural": "Контактные данные",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "name_product",
                    models.CharField(
                        help_text="Укажите название продукта", max_length=255, verbose_name="Название продукта"
                    ),
                ),
                (
                    "model_product",
                    models.CharField(
                        help_text="Укажите модель продукта", max_length=255, verbose_name="Модель продукта"
                    ),
                ),
                (
                    "product_release_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="Укажите дату выхода продукта на рынок",
                        verbose_name="Дата выхода продукта на рынок",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите пользователя, добавившего продукт",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь, добавивший продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.CreateModel(
            name="LinkNetwork",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "name",
                    models.CharField(
                        help_text="Укажите название звена сети", max_length=255, verbose_name="Название звена сети"
                    ),
                ),
                (
                    "level",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "Завод"), (1, "Розничная сеть"), (2, "Индивидуальный предприниматель")],
                        help_text="Укажите уровень звена сети",
                        verbose_name="Уровень звена сети",
                    ),
                ),
                (
                    "debt",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Укажите задолженность перед поставщиком",
                        max_digits=12,
                        verbose_name="Задолженность перед поставщиком",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Дата создания звена сети")),
                (
                    "contact",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите контактные данные",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="trade.contactdata",
                        verbose_name="Контактные данные",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите пользователя, добавившего звено сети",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь, добавивший звено сети",
                    ),
                ),
                (
                    "provider",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите поставщика",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="trade.linknetwork",
                        verbose_name="Поставщик",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите продукт",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="trade.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Звено сети",
                "verbose_name_plural": "Звенья сети",
            },
        ),
    ]
