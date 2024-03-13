from django.shortcuts import render
from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
import os
from django.urls import reverse
# from .forms import *
from .models import *
from django.contrib import messages
import pandas as pd
import plotly.express as px
def home(request):
    return render(request, 'dasbord.html')

def signin(request):
    if request.method == 'POST':
        userName = request.POST.get("inputUsername")
        password = request.POST.get("inputPassword")
        user = authenticate(username=userName, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser == 0:
                emp = Employee.objects.get(userName=userName)
                request.session['userId'] = emp.id
                request.session['userName'] = emp.userName
                request.session['userStatus'] = 'employee'
                return redirect('home')
            else:
                request.session['userId'] = user.id
                request.session['userName'] = user.username
                request.session['userStatus'] = 'admin'
                return redirect('home')
            # messages.add_message(request, messages.INFO, "Login success..")
        else:
            messages.error(request, "User Name or Password not correct..!!!")
            data = {'userName': userName}
            return render(request, 'auth/signin.html', data)
    else:
        return render(request, 'auth/signin.html')

@login_required(login_url='signin')
def signOut(request):
    if request.session.get('userId'):
        del request.session["userId"]
        del request.session["userName"]
        del request.session["userStatus"]
        logout(request)
        return redirect('signin')
    else:
        return redirect('signin')

def changePassword(request):
    userName = request.session.get('userName')
    if request.method == 'POST':
        u = authenticate(username=userName, password=request.POST['oldPassword'])
        if u:
            if request.POST['newPassword'] == request.POST['confirmNewPassword']:
                u.set_password(request.POST['newPassword'])
                u.save()
                messages.add_message(request, messages.INFO, "เปลี่ยนรหัสผ่านเสร็จเรียบร้อย...")
                return redirect('home')
            else:
                messages.add_message(request, messages.WARNING, "รหัสผ่านใหม่กับรหัสที่ยืนยันไม่ตรงกัน...")
                return render(request, 'auth/changePassword.html')
        else:
            messages.add_message(request, messages.WARNING, "รหัสผ่านเก่าไม่ถูกต้อง...")
            return render(request, 'auth/changePassword.html')
    else:
        return render(request, 'auth/changePassword.html')

def stockIn(request):
    return render(request, 'stock/stockIn.html')
def stockOut(request):
    return render(request, 'stock/stockOut.html')

def stockNew(request):
    return render(request, 'stock/stockNew.html')
def stockList(request):
    return render(request, 'stock/stockList.html')
def stockDelete(request):
    return render(request, 'stock/stockDelete.html')
def stockUpdate(request):
    return render(request, 'stock/stockUpdate.html')

def typeNew(request):
    return render(request, 'type/typeNew.html')
def typeList(request):
    return render(request, 'type/typeList.html')
def typeDelete(request):
    return render(request, 'type/typeDelete.html')
def typeUpdate(request):
    return render(request, 'type/typeUpdate.html')

def cusNew(request):
    if request.method == 'POST':
        id = request.POST['inputId']
        fullname = request.POST['inputFullname']
        address = request.POST['inputAddress']
        tell = request.POST['inputTell']
        customer = Customer(id, fullname, address, tell)
        customer.save()
        return redirect('home')
    else:
        return render(request, 'customer/cusNew.html')
def cusList(request):
    customers = Customer.objects.all().order_by('id')
    context = {'customers': customers}
    return render(request, 'customer/cusList.html', context)
def cusDelete(request, id):
    cus = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        cus.delete()
        return redirect('cusList')
    else:
        data = {'cus': cus}
        return render(request, 'customer/cusDelete.html', data)
def cusUpdate(request, id):
    cus = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        fullname = request.POST['inputFullname']
        address = request.POST['inputAddress']
        tell = request.POST['inputTell']
        cus = Customer(id, fullname, address, tell)
        cus.save()
        return redirect('empList')
    else:
        data = {'cus': cus}
        return render(request, 'customer/cusUpdate.html', data)

def empNew(request):
    if request.method == 'POST':
        id = request.POST['inputId']
        username = request.POST['inputUsername']
        email = request.POST['inputEmail']
        fullname = request.POST['inputFullname']
        address = request.POST['inputAddress']
        tell = request.POST['inputTell']
        password = request.POST['inputPassword']
        employee = Employee(id, username, email, fullname, address, tell)
        employee.save()
        user = User.objects.create_user(username, email, password)
        user.first_name = fullname
        user.is_staff = True
        user.save()
        return redirect('home')
    else:
        return render(request, 'employee/empNew.html')
def empList(request):
    employees = Employee.objects.all().order_by('id')
    context = {'employees': employees}
    return render(request, 'employee/empList.html', context)
def empDelete(request, id):
    emp = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        emp.delete()
        return redirect('empList')
    else:
        data = {'emp': emp}
        return render(request, 'employee/empDelete.html', data)
def empUpdate(request, id):
    emp = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        username = request.POST['inputUsername']
        email = request.POST['inputEmail']
        fullname = request.POST['inputFullname']
        address = request.POST['inputAddress']
        tell = request.POST['inputTell']
        emp = Employee( id,username, email, fullname, address, tell)
        emp.save()
        return redirect('empList')
    else:
        data = {'emp': emp}
        return render(request, 'employee/empUpdate.html', data)