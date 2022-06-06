"""reg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from confirm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('account/register/', views.registerpage),
    path('account/registerResult/', views.registerResult),
    path('account/login/', views.loginpage),
    path('account/logout/', views.logout),
    path('account/loginResult/', views.loginResult),
    path('account/myinfo/',views.myinfo),
    path('account/myinfo/save/',views.myinfo_save),
    path('activate/', views.activate),
    path('activate/update/<int:id>', views.activate_update),
    path('activate/delete/<int:id>', views.activate_delete),
    path('contact/', views.contact),
    path('testpage/', views.testpage),
]
