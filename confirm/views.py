from django.shortcuts import render
from django.http import HttpResponse
from .models import UserList
# Create your views here.
def home(request):
    return render(request,'home.html')

def registerpage(request):
    return render(request,'register.html')

def loginpage(request):
    return render(request,'login.html')

def loginResult(request):
    idcard = request.POST.get('idcard')
    birthdate = request.POST.get('birthdate')

    try:
        current = UserList.objects.get(idcard=idcard)
        
        if current.birthdate == birthdate:
            print("TRUE")
            return HttpResponse("TRUE")
        else:
            print("FALSE")
            return HttpResponse("FALSE")
    except UserList.DoesNotExist:
        return HttpResponse("USER DOES NOT EXIST")



def registerResult(request):
    idcard = request.POST.get('idcard')
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    gender = request.POST.get('gender')
    tel = request.POST.get('tel')
    email = request.POST.get('email')
    birthdate = request.POST.get('birthdate')
    type = request.POST.get('type')

    if UserList.objects.filter(idcard=idcard).exists():
        print("DUPLICATE")
    else:
        UserList.objects.create(
        idcard = idcard,
        name = name,
        surname = surname,
        gender = gender,
        tel = tel,
        email = email,
        birthdate = birthdate,
        type = type
        )
    return render(request,'registerResult.html',{'idcard':idcard,'name':name,'surname':surname,'gender':gender,'tel':tel,'email':email,'birthdate':birthdate,'type':type})