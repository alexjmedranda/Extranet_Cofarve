"""Extranet_Cofarve URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from blog.views import inicio, administrador, galeria,actualizar, delete, update, delete2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio, name= 'index'),
    path('administrador/',administrador, name= 'admin'),
    path('galeria/',galeria, name= 'galeria'),
    path('administrador/send/',actualizar, name= 'actualizar'),
    path('delete/<int:pk>', delete, name="delete"),
    path('administrador/update/<int:id>', update, name="update"), 
    path('deleteSubmenu/<int:pk>', delete2, name='delete2',)

]

