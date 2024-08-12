from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser

from trade.filters import CountryFilter
from trade.models import LinkNetwork
from trade.permissions import IsOwner
from trade.serializers import LinkNetworkSerializer, LinkNetworkDetailSerializer


class LinkNetworkCreateAPIView(CreateAPIView):
    queryset = LinkNetwork.objects.all()
    serializer_class = LinkNetworkSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LinkNetworkListAPIView(ListAPIView):
    queryset = LinkNetwork.objects.all()
    serializer_class = LinkNetworkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CountryFilter
    permission_classes = [IsAdminUser | IsOwner]

    def get_queryset(self):
        return LinkNetwork.objects.filter(owner=self.request.user)


class LinkNetworkRetrieveAPIView(RetrieveAPIView):
    queryset = LinkNetwork.objects.all()
    serializer_class = LinkNetworkDetailSerializer
    permission_classes = [IsAdminUser | IsOwner]


class LinkNetworkUpdateAPIView(UpdateAPIView):
    queryset = LinkNetwork.objects.all()
    serializer_class = LinkNetworkSerializer
    permission_classes = [IsAdminUser | IsOwner]


class LinkNetworkDestroyAPIView(DestroyAPIView):
    queryset = LinkNetwork.objects.all()
    serializer_class = LinkNetworkSerializer
    permission_classes = [IsAdminUser | IsOwner]
