from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=100)
    src = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Side(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100)
    type = models.ManyToManyField(Type, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    qtity = models.IntegerField(default=0)
    img = models.CharField(max_length=100)
    side = models.ManyToManyField(Side, blank=True)
    
    def __str__(self):
        return self.name
    
    
class FoodOrder(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=2)
    food = models.ManyToManyField(Food, blank=True)
    name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f'Order: {self.id}'