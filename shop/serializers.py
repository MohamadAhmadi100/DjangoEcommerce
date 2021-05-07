from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    sub_category = serializers.StringRelatedField()

    class Meta:
        model = Category
        fields = ('id', 'sub_category', 'name', 'slug', 'is_sub')


class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(source='category', many=True)

    class Meta:
        model = Product
        fields = ('id', 'categories', 'name', 'slug', 'description', 'price', 'inventory', 'created', 'updated', 'code')
