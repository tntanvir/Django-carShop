from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ModelForm
from .models import carModel


from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
# def carBrand(request):
#     if request.method=='POST':
#         forms=ModelForm(request.POST)
#         if forms.is_valid():
#             forms.save()
#     else:
#         forms=ModelForm()
#     return render(request, 'carBrand.html', {'forms':forms})

class CarBrand(CreateView):
    model = carModel
    form_class= ModelForm
    template_name = 'carBrand.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        return super().form_valid(form)