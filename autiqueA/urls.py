"""
URL configuration for autiqueA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from autiqueApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard', views.home, name = 'home'),
    path('', views.signin, name = 'signin'),
    path('signout', views.signOut, name = 'signout'),
    path('changepassword', views.changePassword, name = 'changePassword'),

    path('stockIn/new', views.stockInNew, name = 'stockInNew'),
    path('stockIn/list', views.stockInList, name = 'stockInList'),

    path('stockout/stockout', views.stockOut, name = 'stockOutList'),
    path('stockout/sell/<id>', views.stockSell, name = 'stockSell'),

    path('stock/new', views.stockNew, name = 'stockNew'),
    path('stock/list', views.stockList, name = 'stockList'),
    path('stock/delete/<id>', views.stockDelete, name='stockDelete'),
    path('stock/update/<id>', views.stockUpdate, name='stockUpdate'),

    path('type/new', views.typeNew, name = 'typeNew'),
    path('type/list', views.typeList, name = 'typeList'),
    path('type/delete/<id>', views.typeDelete, name='typeDelete'),
    path('type/update/<id>', views.typeUpdate, name='typeUpdate'),

    path('customer/new', views.cusNew, name = 'cusNew'),
    path('customer/list', views.cusList, name = 'cusList'),
    path('customer/delete/<id>', views.cusDelete, name = 'cusDelete'),
    path('customer/update/<id>', views.cusUpdate, name = 'cusUpdate'),

    path('employee/new', views.empNew, name = 'empNew'),
    path('employee/list', views.empList, name = 'empList'),
    path('employee/delete/<id>', views.empDelete, name = 'empDelete'),
    path('employee/update/<id>', views.empUpdate, name = 'empUpdate'),


]
