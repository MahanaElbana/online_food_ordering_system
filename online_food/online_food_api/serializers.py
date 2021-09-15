from rest_framework import serializers
from .models import Category, Restaurant, Menu, Customer, Order, Reservation, Reating


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name','description','created']


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id','cat_id','name','email','phone',
                  'url','open_hours','close_hours','address','image']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','rest_id','name','price','about','image']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','first_name','last_name','email','password',
                  'phone','address',]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','name','quantity','price','created']



class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id','order_id','customer_id']


class ReatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reating
        fields = ['id','menu_id','customer_id']

