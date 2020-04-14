from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Mall(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    catName = models.CharField(max_length=100)

    def __str__(self):
        return self.catName


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    discount = models.IntegerField(null=True)
    owner = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE, null=True)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    mallId = models.ForeignKey(Mall, on_delete=models.CASCADE, null=True)
