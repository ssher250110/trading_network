from rest_framework.serializers import ValidationError


class ProviderValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, link_network):
        provider = link_network.get(self.field)
        name = link_network.get("name")
        level = link_network.get("level")
        if provider:
            if provider.name == name:
                raise ValidationError("Нельзя выбрать себя в качестве поставщика")
            elif level == 0 and provider.level != 0:
                raise ValidationError(
                    "У завода не может быть поставщиков, уровня розничная сеть и индивидуальный предприниматель"
                )
            elif level == 1 and provider.level == 2:
                raise ValidationError("Индивидуальный предприниматель не может быть поставщиком для розничной сети")
            elif level == 2 and provider.level != 2:
                raise ValidationError(
                    "Индивидуальный предприниматель может быть поставщиком,"
                    "только другому индивидуальному предпринимателю"
                )
