import django_filters
from trade.models import LinkNetwork


class CountryFilter(django_filters.rest_framework.FilterSet):
    """Кастомный класс для поиска по стране"""

    country = django_filters.CharFilter(field_name="contact_country", lookup_expr="icontains")

    class Meta:
        model = LinkNetwork
        fields = ["country"]
