from django.db import models

# Create your models here.
from django.db import models
from django.contrib.postgres.fields import ArrayField
from custom_user.models import Organization

class Tables(models.Model):
    number          =   models.IntegerField(default=0)
    capacity        =   models.IntegerField(default=0)
    hotel           =   models.ForeignKey(to=Organization, on_delete=models.CASCADE, default="", null=True)

class Menu(models.Model):
    hotel           =   models.ForeignKey(to=Organization, on_delete=models.CASCADE, default="", null=True)

class Section(models.Model):
    name            =   models.CharField(max_length=100)
    menu            =   models.ForeignKey(to=Menu, on_delete=models.CASCADE, default="", null=True)

class Items(models.Model):
    name            =   models.CharField(max_length=100)
    description     =   models.CharField(max_length=100)
    price           =   models.IntegerField(default=0)
    tags            =   ArrayField(models.CharField(max_length=1000, blank=False), default=list)
    menu            =   models.ForeignKey(to=Menu, on_delete=models.CASCADE, default="", null=True)
    section         =   models.ForeignKey(to=Section, on_delete=models.CASCADE, default="", null=True)
    hotel           =   models.ForeignKey(to=Organization, on_delete=models.CASCADE, default="", null=True)

class Order(models.Model):
    table           =   models.ForeignKey(to=Tables, on_delete=models.CASCADE, default="", null=True)
    state           =   models.CharField(max_length=100)
    read            =   models.BooleanField()

class OrderItemMap(models.Model):
    order           =   models.ForeignKey(to=Order, on_delete=models.CASCADE)
    item            =   models.ForeignKey(to=Items, on_delete=models.CASCADE)
    quantity        =   models.IntegerField(default=1)