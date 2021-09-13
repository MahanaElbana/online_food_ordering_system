from rest_framework import serializers
from .models import Category, Restaurant, Menu, Customer, Order, Reservation, Reating


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name', 'description', 'created']
