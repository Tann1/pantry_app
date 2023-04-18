from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length = 25)
    email    = models.CharField(max_length = 200)
    password = models.charField(max_length = 256)

class ingredients(models.Model):
    name     = models.CharField(max_length = 150)
    category = models.CharField(max_length = 150)
    unit     = models.CharField(max_length = 25)
    calories = models.IntegerField(default = 0)

class pantry(models.Model):
    user_id       = models.ForeignKey(users, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(ingredients, on_delete=models.CASCADE)
    quantity      = models.IntegerField(default=0)