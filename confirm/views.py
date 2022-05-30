from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def registerpage(request):
    return render(request,'register.html')

def loginpage(request):
    return render(request,'login.html')

def registerResult(request):
    idcard = request.POST.get('idcard')
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    gender = request.POST.get('gender')
    tel = request.POST.get('tel')
    email = request.POST.get('email')
    birthdate = request.POST.get('birthdate')
    type = request.POST.get('type')
    
    return render(request,'registerResult.html',{'idcard':idcard,'name':name,'surname':surname,'gender':gender,'tel':tel,'email':email,'birthdate':birthdate,'type':type})