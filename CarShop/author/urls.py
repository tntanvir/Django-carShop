from django.urls import path,include
from . import views

urlpatterns = [
    path('singup/',views.singup.as_view(),name='singup'),
    path('singin/',views.singin,name='singin'),
    path('singout/',views.logoutUser,name='singout'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.profileEdit.as_view(),name='profileEdit'),
    
]