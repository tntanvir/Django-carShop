from django.shortcuts import render,redirect
from .forms import CarModelForm

# Create your views here.
def car(request):
    if request.method =='POST':
        forms=CarModelForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.instance.author=request.user
            forms.save()
            return redirect('home')
    else:
        forms=CarModelForm()
    return render(request, 'car.html', {'forms':forms})