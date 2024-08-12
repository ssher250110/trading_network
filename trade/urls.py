from django.urls import path

from trade.apps import TradeConfig
from trade.views import LinkNetworkCreateAPIView, LinkNetworkListAPIView, LinkNetworkRetrieveAPIView, \
    LinkNetworkUpdateAPIView, LinkNetworkDestroyAPIView

app_name = TradeConfig.name

urlpatterns = [
    path('link/create/', LinkNetworkCreateAPIView.as_view(), name='link-create'),
    path('link/', LinkNetworkListAPIView.as_view(), name='link-list'),
    path('link/<int:pk>/', LinkNetworkRetrieveAPIView.as_view(), name='link-retrieve'),
    path('link/<int:pk>/update/', LinkNetworkUpdateAPIView.as_view(), name='link-update'),
    path('link/<int:pk>/destroy/', LinkNetworkDestroyAPIView.as_view(), name='link-destroy'),
]