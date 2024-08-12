import django_filters
from trade.models import LinkNetwork


class CityFilter(django_filters.rest_framework.FilterSet):

    title = django_filters.CharFilter(field_name="city", lookup_expr="icontains")

    class Meta:
        model = LinkNetwork
        fields = ["city"]
