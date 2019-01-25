from django.db import models
from django.urls import reverse

# Create your models here.


class Winery(models.Model):
    winery_name = models.CharField(max_length=250)
    winery_location = models.CharField(max_length=250)
    winery_picture = models.FileField(default='')

    def get_absolute_url(self):
        return reverse('Wine:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.winery_name + ' - ' + self.winery_location


class Wine(models.Model):
    winery = models.ForeignKey(Winery, on_delete=models.CASCADE)
    wine_name = models.CharField(max_length=250)
    wine_color = models.CharField(max_length=250)
    wine_varietal = models.CharField(max_length=250)
    wine_abv = models.CharField(max_length=250)
    is_favorite = models.BooleanField(False)
    wine_picture = models.FileField(default='')

    def __str__(self):
        return self.wine_name
