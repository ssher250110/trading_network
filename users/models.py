from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager

NULLABLE = {"null": True, "blank": True}


class UserRoles(models.TextChoices):
    USER = "user", _("Пользователь")
    ADMIN = "admin", _("Администратор")


class User(AbstractBaseUser):
    """Модель для создания пользователя"""

    username = None
    email = models.EmailField(unique=True, verbose_name="Почта", help_text="Укажите электронную почту")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия", help_text="Укажите фамилию")
    first_name = models.CharField(max_length=255, verbose_name="Имя", help_text="Укажите имя")
    middle_name = models.CharField(max_length=255, verbose_name="Отчество", help_text="Укажите отчество")
    phone = models.CharField(max_length=15, verbose_name="Телефон", help_text="Укажите телефон для связи")
    role = models.CharField(
        max_length=5,
        choices=UserRoles,
        default=UserRoles.USER,
        verbose_name="Роль",
        help_text="Укажите роль пользователя",
    )
    image = models.ImageField(
        upload_to="users/image", **NULLABLE, verbose_name="Фотография", help_text="Разместите Вашу фотографию"
    )
    is_active = models.BooleanField(
        default=True, verbose_name="Активация", help_text="Укажите активен ли пользователь"
    )
    last_login = models.DateTimeField(_("last login"), **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["last_name", "first_name", "middle_name", "phone", "image"]

    @staticmethod
    def update_last_login(user, **kwargs):
        user.last_login = timezone.now()
        user.save(update_fields=["last_login"])

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["email"]
