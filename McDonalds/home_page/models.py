from django.db import models
from django.urls import reverse
# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    chef = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:details',kwargs={'pk':self.pk})

class Workers(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    restaurant = models.ForeignKey(Restaurant,related_name='workers',on_delete="cascade")

    def __str__(self):
        return self.name
