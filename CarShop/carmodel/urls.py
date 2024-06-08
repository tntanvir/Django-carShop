from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarBrand.as_view(),name='carBrand'),
]