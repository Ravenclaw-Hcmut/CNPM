from rest_framework import serializers

from .models import Food, Type, Side, FoodOrder

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
        

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Type
        fields = '__all__'
        

class SideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Side
        fields = '__all__'
        

class FoodOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodOrder
        fields = '__all__'