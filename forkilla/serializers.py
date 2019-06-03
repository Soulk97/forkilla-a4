from .models import Restaurant
from rest_framework import serializers


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = (
            'restaurant_number', 'name', 'menu_description',
            'price_average', 'is_promot', 'rate', 'address',
            'city', 'country', 'featured_photo', 'category',
            'capacity'
        )

