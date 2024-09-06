from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from trade.filters import CountryFilter
from trade.models import ContactData, LinkNetwork, Product
from trade.permissions import IsOwner
from trade.serializers import (
    ContactDataSerializer,
    LinkNetworkSerializer,
    LinkNetworkDetailSerializer,
    LinkNetworkUpdateSerializer,
    ProductSerializer,
)


class ContactDataViewSet(ModelViewSet):
    """Набор связанных представлений модели контактные данные"""

    queryset = ContactData.objects.all()
    serializer_class = ContactDataSerializer

    def perform_create(self, serializer):
        """Добавление создателя контактных данных"""

        serializer.save(creator=self.request.user)

    def get_permissions(self):
        """Получение прав доступа по условиям"""

        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["retrieve", "list"]:
            self.permission_classes = [IsAuthenticated]
        elif self.action == ["destroy", "update"]:
            self.permission_classes = [IsAdminUser | IsOwner]
        return super().get_permissions()


class ProductViewSet(ModelViewSet):
    """Набор связанных представлений модели продукт"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """Добавление создателя продукта"""

        serializer.save(creator=self.request.user)

    def get_permissions(self):
        """Получение прав доступа по условиям"""

        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["retrieve", "list"]:
            self.permission_classes = [IsAuthenticated]
        elif self.action == ["destroy", "update"]:
            self.permission_classes = [IsAdminUser | IsOwner]
        return super().get_permissions()


class LinkNetworkCreateAPIView(CreateAPIView):
    """Создание звена сети"""

    queryset = LinkNetwork.objects.all()
    serializer_class = LinkNetworkSerializer

    def perform_create(self, serializer):
        """Добавление пользователя создавшего звено сети"""

        serializer.save(creator=self.request.user)


class LinkNetworkListAPIView(ListAPIView):
    """Просмотр списка звеньев сети"""

    queryset = LinkNetwork.objects.all()
    serializer_class = LinkNetworkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CountryFilter
    permission_classes = [IsAdminUser | IsOwner]

    def get_queryset(self):
        """Получение набора данных по условию"""

        return LinkNetwork.objects.filter(creator=self.request.user)


class LinkNetworkRetrieveAPIView(RetrieveAPIView):
    """Просмотр одного звена сети"""

    queryset = LinkNetwork.objects.all()
    serializer_class = LinkNetworkDetailSerializer
    permission_classes = [IsAdminUser | IsOwner]


class LinkNetworkUpdateAPIView(UpdateAPIView):
    """Обновление звена сети"""

    queryset = LinkNetwork.objects.all()
    serializer_class = LinkNetworkUpdateSerializer
    permission_classes = [IsAdminUser | IsOwner]


class LinkNetworkDestroyAPIView(DestroyAPIView):
    """Удаление звена сети"""

    queryset = LinkNetwork.objects.all()
    serializer_class = LinkNetworkSerializer
    permission_classes = [IsAdminUser | IsOwner]
