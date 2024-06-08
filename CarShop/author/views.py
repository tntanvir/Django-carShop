from django.shortcuts import render,redirect
from .forms import CreateUserForm,UpdateUserForm
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from car.models import OderCar
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User 

# Create your views here.
# def singup(request):
#     if request.method =="POST":
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = CreateUserForm()
#     return render(request,'auth.html',{'forms':form,type:'singup'})
class singup(CreateView):
    form_class = CreateUserForm
    template_name = 'auth.html'
    success_url = reverse_lazy('singin')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] ='singup'
        return context

def singin(request):
    if request.method =="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request,'auth.html',{'form':form,type:'singin'})
def profile(request):
    order=OderCar.objects.filter(user=request.user)
    return render(request,'profile.html',{'order':order})

# def profileEdit(request):
#     if request.method =="POST":
#         form = UpdateUserForm(request.POST,instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = UpdateUserForm(instance=request.user)
#     return render(request,'profileEdit.html',{'forms':form})
class profileEdit(UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'profileEdit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

def logoutUser(request):
    logout(request)
    return redirect('singin')