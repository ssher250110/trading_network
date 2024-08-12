import django_filters
from trade.models import LinkNetwork


class CountryFilter(django_filters.rest_framework.FilterSet):
    title = django_filters.CharFilter(field_name="country", lookup_expr="icontains")

    class Meta:
        model = LinkNetwork
        fields = ["country"]
