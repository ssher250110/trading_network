import django_filters
from trade.models import ContactData


class CountryFilter(django_filters.rest_framework.FilterSet):
    """Кастомный класс для поиска по стране"""

    title = django_filters.CharFilter(field_name="country", lookup_expr="icontains")

    class Meta:
        model = ContactData
        fields = ["country"]
