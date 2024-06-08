from django.contrib import admin
from .models import Car,CarComment,OderCar

# Register your models here.
admin.site.register(Car)
admin.site.register(CarComment)
admin.site.register(OderCar)