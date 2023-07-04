from django.db import models

# Create your models here.
class List(models.Model) :
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.name