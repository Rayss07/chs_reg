from django.shortcuts import render
from django.http import HttpResponse
from ..models import UserList , Info_Basic
from django.shortcuts import redirect
from django.contrib.sessions.backends.db import SessionStore

def testpage(request):
    return render(request,'test.html')

def home(request):
    idcard = request.session.get('current_user')
    data = UserList.objects.filter(idcard=idcard)
    return render(request,'home.html',{'user':data})

def register(request):
    if request.method != "POST":
        return render(request,'register.html')
    else:
        idcard = request.POST.get('idcard')
        prefix = request.POST.get('prefix')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        gender = request.POST.get('gender')
        tel = request.POST.get('tel')
        email = request.POST.get('email')
        birthdate = request.POST.get('birthdate')
        type = "นักเรียน"

        if UserList.objects.filter(idcard=idcard).exists():
            return render(request,'register.html',{'status':"มีเลขประจำตัวผู้ใช้งานนี้ในระบบแล้ว"})
        else:
            UserList.objects.create(
            idcard = idcard,
            prefix = prefix,
            name = name,
            surname = surname,
            gender = gender,
            tel = tel,
            email = email,
            birthdate = birthdate,
            type = type
            )
            return render(request,'registerResult.html',{'idcard':idcard,'prefix':prefix,'name':name,'surname':surname,'gender':gender,'tel':tel,'email':email,'birthdate':birthdate,'type':type})        

def login(request):
    if request.method != "POST":
        return render(request,'login.html')
    else:
        idcard = request.POST.get('idcard')
        birthdate = request.POST.get('birthdate')

        try:
            current = UserList.objects.get(idcard=idcard)
            
            if current.birthdate == birthdate:
                request.session['current_user'] = idcard
                return redirect('/')
            else:
                print("FALSE")
                return render(request,'login.html',{'status':"รหัสผ่านผิด"})
        except UserList.DoesNotExist:
            return render(request,'login.html',{'status':"ไม่พบผู้ใช้"})

def logout(request):
    try:
        del request.session['current_user']
    except KeyError:
        pass
    return redirect('/')

###############################Rewrite


def contact(request):
    idcard = request.session.get('current_user')
    data = UserList.objects.filter(idcard=idcard)
    return render(request,'contact.html',{'user':data})



def activate(request):
    idcard = request.session.get('current_user')
    cur = UserList.objects.get(idcard=idcard)
    current = UserList.objects.filter(idcard=idcard)
    alluser = UserList.objects.filter(activated=0)
    if cur.type == "เจ้าหน้าที่":
        return render(request,'activate.html',{'user':current,'alluser':alluser})
    else:
        return redirect('/')

def activate_update(request,id):
    selected_user = UserList.objects.get(idcard=id)
    selected_user.activated = 1
    selected_user.save()
    return redirect('/activate')

def activate_delete(request,id):
    selected_user = UserList.objects.get(idcard=id)
    selected_user.delete()
    return redirect('/activate')

def myinfo(request):
    idcard = request.session.get('current_user')
    data = UserList.objects.filter(idcard=idcard)
    return render(request,'myinfo.html',{'user':data})

def myinfo_save(request,id):
    pass

