from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Item, Mall, Category


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'discount', 'categoryId', 'mallId']


class MallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mall
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'catName']
