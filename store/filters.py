import django_filters
from .models import Product

class ProductFilterSet(django_filters.FilterSet):

    class Meta:
        model = Product

        # Fields on which will be presented as form
        fields = (
            'name',
            'price',
            'seller',
            'category'
        )