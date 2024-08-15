from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Info

# Create your views here.
def home(request):
    my=Info.objects.all()
    if my!="":
        return render(request,'home.html',{'dar':my})
    else:
       return render(request,'home.html')
def addData(request):
    if  request.method=="POST":
        name=request.POST["name"]
        age=request.POST["age"]
        dateofbirth=request.POST["dateofbirth"]
        phonenumber=request.POST["phonenumber"]
        address=request.POST["address"]
        mail=request.POST["mail"]
        
        
        
        obj=Info()
        obj.Name=name
        obj.Age=age
        obj.DateOfBirth=dateofbirth
        obj.PhoneNumber=phonenumber
        obj.Address=address
        obj.Mail=mail
        obj.save()
        return redirect('home')
    return render(request,'home.html')
def updateData(request,id):
    my=Info.objects.get(id=id)
    if request.method=="POST":
        name=request.POST["name"]
        age=request.POST["age"]
        dateofbirth=request.POST["dateofbirth"]
        phonenumber=request.POST["phonenumber"]
        address=request.POST["address"]
        mail=request.POST["mail"]
        my.Name=name
        my.Age=age
        my.DateOfBirth=dateofbirth
        my.PhoneNumber=phonenumber
        my.Address=address
        my.Mail=mail
        my.save()
        return redirect('home')
    return render(request,'update.html',{'data':my})
def deleteData(request,id):
    my=Info.objects.get(id=id)
    my.delete()
    return redirect('home')


    
        
        
        

        
    
        
