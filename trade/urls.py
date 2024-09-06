from django.urls import include, path
from rest_framework.routers import SimpleRouter

from trade.apps import TradeConfig
from trade.views import (
    ContactDataViewSet,
    LinkNetworkCreateAPIView,
    LinkNetworkListAPIView,
    LinkNetworkRetrieveAPIView,
    LinkNetworkUpdateAPIView,
    LinkNetworkDestroyAPIView,
    ProductViewSet,
)

contact_data_router = SimpleRouter()
contact_data_router.register("contact_data", ContactDataViewSet, basename="contact_data")

product_router = SimpleRouter()
product_router.register("product", ProductViewSet, basename="product")

app_name = TradeConfig.name

urlpatterns = [
    path("", include(contact_data_router.urls)),
    path("", include(product_router.urls)),
    path("link/create/", LinkNetworkCreateAPIView.as_view(), name="link-create"),
    path("link/", LinkNetworkListAPIView.as_view(), name="link-list"),
    path("link/<int:pk>/", LinkNetworkRetrieveAPIView.as_view(), name="link-retrieve"),
    path("link/<int:pk>/update/", LinkNetworkUpdateAPIView.as_view(), name="link-update"),
    path("link/<int:pk>/destroy/", LinkNetworkDestroyAPIView.as_view(), name="link-destroy"),
]
