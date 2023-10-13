from django.db import models
from django.contrib.auth.models import User
import random

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    order_number = models.CharField(max_length=13, unique=True, blank=True)
    address_line1 = models.CharField(max_length=50, blank=True)
    address_line2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank= True)
    state = models.CharField(max_length=50, blank= True)
    zip = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = random.randint(100000, 999999)
            self.id = self.order_number  # Set the id field to the order_number value
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

"""
I debated making this into a simple function but I think the data model is a better solution.
Using a data model we have the ability to go back edit the discount code or add more codes.
Using a function to generate the codes would not actually store them anywhere. and they would have
to be evaluated by the view at run time.
"""
class DCode(models.Model):
    code = models.CharField(max_length=24)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.code