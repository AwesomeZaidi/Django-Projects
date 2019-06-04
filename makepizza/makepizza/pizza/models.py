from django.db import models

class Topping(models.Model):
    name = models.CharField(max_length=28)
    size = models.CharField(max_length=28)
    price = models.CharField(max_length=28)

class Pizza(models.Model):
    name = models.CharField(max_length=28)    
    toppings = models.ManyToManyField(Topping)
    size = models.CharField(max_length=28)
    price = models.CharField(max_length=28)

class Order(models.Model):
    orderNumber = models.CharField(max_length=28)
    toppingsCost = models.OneToManyField(models.ForeignKey(Topping))
    pizzasCost = models.OneToManyField(models.ForeignKey(Pizza))
    totalCost = toppingsCost + pizzasCost

