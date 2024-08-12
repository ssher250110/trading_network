from rest_framework.serializers import ModelSerializer

from trade.models import LinkNetwork
from trade.validators import ProviderValidator


class LinkNetworkSerializer(ModelSerializer):
    class Meta:
        model = LinkNetwork
        fields = "__all__"
        validators = [ProviderValidator(field="provider")]


class LinkNetworkDetailSerializer(ModelSerializer):
    class Meta:
        model = LinkNetwork
        exclude = ["owner"]
        depth = 1


class LinkNetworkUpdateSerializer(ModelSerializer):
    class Meta:
        model = LinkNetwork
        exclude = ["debt"]
        validators = [ProviderValidator(field="provider")]
