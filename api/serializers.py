from dataclasses import field, fields
from rest_framework import serializers

from api import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
    
    def create(self, validated_data):
        return models.Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()
        return instance
    
    def get_queryset(self):
        return models.Category.objects.all()
    
    def get_object(self):
        return models.Category.objects.get(pk=self.kwargs.get('pk'))

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Price
        fields = '__all__'
    
    def create(self, validated_data):
        return models.Price.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()
        return instance
    
    def get_queryset(self):
        return models.Price.objects.all()
    
    def get_object(self):
        return models.Price.objects.get(pk=self.kwargs.get('pk'))
    
class UtensilSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Utensil
        fields = '__all__'
    
    def create(self, validated_data):
        return models.Utensil.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()
        return instance
    
    def get_queryset(self):
        return models.Utensil.objects.all()
    
    def get_object(self):
        return models.Utensil.objects.get(pk=self.kwargs.get('pk'))
    
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = '__all__'
    
    def create(self, validated_data):
        return models.Ingredient.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()
        return instance
    
    def get_queryset(self):
        return models.Ingredient.objects.all()
    
    def get_object(self):
        return models.Ingredient.objects.get(pk=self.kwargs.get('pk'))
    
class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Measure
        fields = '__all__'
    
    def create(self, validated_data):
        return models.Measure.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()
        return instance
    
    def get_queryset(self):
        return models.Measure.objects.all()
    
    def get_object(self):
        return models.Measure.objects.get(pk=self.kwargs.get('pk'))
    
class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Difficulty
        fields = '__all__'
    
    def create(self, validated_data):
        return models.Difficulty.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()
        return instance
    
    def get_queryset(self):
        return models.Difficulty.objects.all()
    
    def get_object(self):
        return models.Difficulty.objects.get(pk=self.kwargs.get('pk'))
    
    
    