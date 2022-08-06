from rest_framework import viewsets

from api import serializers, models
  
class CategoryViewSet(viewsets.ModelViewSet):
    """ Create and update categories """

    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    
class PriceViewSet(viewsets.ModelViewSet):
    """ Create and update price """

    serializer_class = serializers.PriceSerializer
    queryset = models.Price.objects.all()
    
class UtensilViewSet(viewsets.ModelViewSet):
    """ Create and update Utensil """

    serializer_class = serializers.UtensilSerializer
    queryset = models.Utensil.objects.all()

class IngredientViewSet(viewsets.ModelViewSet):
    """ Create and update ingredient """

    serializer_class = serializers.IngredientSerializer
    queryset = models.Ingredient.objects.all()
    
class MeasureViewSet(viewsets.ModelViewSet):
    """ Create and update measure """

    serializer_class = serializers.MeasureSerializer
    queryset = models.Measure.objects.all()

class DifficultyViewSet(viewsets.ModelViewSet):
    """ Create and update difficulty """

    serializer_class = serializers.DifficultySerializer
    queryset = models.Difficulty.objects.all()

