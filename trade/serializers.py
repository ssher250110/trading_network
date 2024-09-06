from rest_framework.serializers import ModelSerializer

from trade.models import ContactData, LinkNetwork, Product
from trade.validators import ProviderValidator


class ContactDataSerializer(ModelSerializer):
    """Сериализатор контактных данных"""

    class Meta:
        model = ContactData
        fields = ["id", "email", "country", "city", "street", "house_number", "creator"]


class ProductSerializer(ModelSerializer):
    """Сериализатор продукта"""

    class Meta:
        model = Product
        fields = ["id", "name_product", "model_product", "product_release_date", "creator"]


class LinkNetworkSerializer(ModelSerializer):
    """Сериализатор звена сети"""

    class Meta:
        model = LinkNetwork
        fields = ["id", "name", "contact", "product", "level", "provider", "debt", "created_at", "creator"]
        validators = [ProviderValidator(field="provider")]


class LinkNetworkDetailSerializer(ModelSerializer):
    """Сериализатор детальной информации о звене сети"""

    class Meta:
        model = LinkNetwork
        exclude = ["creator"]
        depth = 1


class LinkNetworkUpdateSerializer(ModelSerializer):
    """Сериализатор обновления информации о звене сети без поля задолженности"""

    class Meta:
        model = LinkNetwork
        exclude = ["debt"]
        validators = [ProviderValidator(field="provider")]
