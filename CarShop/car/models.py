from django.db import models
from carmodel.models import carModel
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    image = models.ImageField(upload_to='car/images/',blank=True, null=True)
    name = models.CharField(max_length=100)
    price=models.FloatField()
    brand= models.ForeignKey(carModel,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    discription=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)


class CarComment(models.Model):
    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    comment=models.TextField()

class OderCar(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    car=models.ForeignKey(Car,on_delete=models.CASCADE)