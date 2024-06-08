from django.shortcuts import render,redirect
from car.models import Car,CarComment,OderCar
from car.forms import CarCommentForm
from carmodel.models import carModel

# Create your views here.
#Home
# def home(request):
#     data=Car.objects.all()
#     return render(request,'home.html',{'data':data})


def home(request, category_slug = None):
    data = Car.objects.all()
    if category_slug is not None:
        category = carModel.objects.get(slug = category_slug)
        data = Car.objects.filter(brand  = category)
    categories = carModel.objects.all()
    return render(request, 'home.html', {'data' : data, 'category' : categories})

def carDetails(request,id):
    data=Car.objects.get(id=id)
    carcomment=CarComment.objects.filter(car=data)
    if request.method=='POST':
        commentForm=CarCommentForm(request.POST)
        if commentForm.is_valid():
            comment=commentForm.save(commit=False)
            comment.car=data
            comment.save()
            return redirect('carDetails',id=id)
    else:
        commentForm=CarCommentForm()
    return render(request,'CarDtaile.html',{'data':data,'commentForm':commentForm,'allcomments':carcomment})



def carUpdate(request,id):
    if request.method =='POST':
        car=Car.objects.get(id=id)
        car.quantity-=1
        car.save()
        order=OderCar.objects.create(user=request.user,car=car)
        order.save()
        return redirect('carDetails',id=id)
    else:
        return redirect('carDetails',id=id)
    