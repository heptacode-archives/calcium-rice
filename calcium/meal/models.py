from django.db import models

class Meal(models.Model):
    date = models.DateField(primary_key=True)
    meal = models.CharField(max_length=200)
    allergyCodes = models.CharField(max_length=200)
    allergicFoods = models.CharField(max_length=200)
    img = models.URLField(),

    def __str__(self):
        return self.date