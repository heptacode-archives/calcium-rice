from django.db import models

class Meal(models.Model):
    meal = models.CharField()
    allergyCodes = models.CharField()
    allergicFoods = models.CharField()
    img = models.URLField(max_length=200, default='https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/SunrinInternetHighSchool.png/900px-SunrinInternetHighSchool.png')

    def __str__(self):
        return self.name
