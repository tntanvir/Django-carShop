from django.db import models

# Create your models here.
class carModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100,unique=True)
    def __str__(self) -> str:
        return self.name