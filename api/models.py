from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name

class Price(models.Model):
    name = models.CharField(max_length=50)

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

class Utensil(models.Model):
    name = models.CharField(max_length=50)
    
class Difficulty(models.Model):
    name = models.CharField(max_length=50)

class Measure(models.Model):
    name = models.CharField(max_length=50)


