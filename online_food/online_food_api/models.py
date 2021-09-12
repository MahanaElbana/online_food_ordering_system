from django.db import models

# Create your models here.

class Menu(models.Model):
    rest_id = models.ForeignKey("Restaurant", on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    about = models.TextField()
    image = models.ImageField(upload_to='menu/%Y/%m/%d/')
    
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    url = models.URLField(max_length=200)
    open_hours = models.IntegerField()
    close_hours = models.IntegerField()
    address = models.CharField(max_length=150)
    image = models.ImageField(upload_to='restaurent/%Y/%m/%d/')

    def __str__(self):
        return self.name
        
class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    reservate = models.ManyToManyField('Order', through='Reservation')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Reservation(models.Model):
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Order(models.Model):
    name = models.CharField(max_length=150)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    # item : i don't what it mean
    def __str__(self):
        return self.name
