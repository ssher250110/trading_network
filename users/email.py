from django.contrib.auth.tokens import default_token_generator
from templated_mail.mail import BaseEmailMessage

from djoser import utils
from djoser.conf import settings


class PasswordResetEmail(BaseEmailMessage):
    """Класс для сброса пароля, через электронную почту"""

    def get_context_data(self):
        """Формирование ссылки для отправки пользователю"""

        context = super().get_context_data()
        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.PASSWORD_RESET_CONFIRM_URL.format(**context)
        return context
