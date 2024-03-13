import json

from django.shortcuts import render
from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal
import os
from django.urls import reverse
# from .forms import *
from .models import *
from django.contrib import messages
import pandas as pd
import plotly.express as px


@login_required(login_url='signin')
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


@login_required(login_url='signin')
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

from django.http import JsonResponse
@login_required(login_url='signin')
def stockInNew(request):
    if request.method == 'POST':
        cus_id = request.POST.get('cus_id')
        purchase_items = request.POST.get('purchase_items')

        purchase_items = json.loads(purchase_items)

        customer, _ = Customer.objects.get_or_create(id=cus_id)

        total = 0

        for item in purchase_items:
            type_id = int(item['type_id'])
            amount = int(item['amount'])

            order = ReceiveOrder.objects.create()

            if not InventoryStock.objects.filter(type_id=type_id).exists():
                inventory = InventoryStock.objects.create(type_id=type_id, totalAmount=amount)
            else:
                inventory = InventoryStock.objects.get(type_id=type_id)
                inventory.totalAmount += amount
                inventory.save()

            detail = ReceiveDetail.objects.create(
                inv_id=inventory,
                amount=amount,
                total=inventory.type_id.rateReceive * amount,
                cus_id=customer,
                order_id=order.id
            )

            total += detail.total

        order.total = total
        order.save()

        if request.is_ajax():
            return JsonResponse({'success': True})
        else:
            return redirect('stockInList')

    types = Type.objects.all().order_by('id')
    cuss = Customer.objects.all().order_by('id')
    context = {'types': types, 'cuss': cuss}
    return render(request, 'stock/stockInNew.html', context)


@login_required(login_url='signin')
def stockInList(request):
    return render(request, 'stock/stockInList.html')


@login_required(login_url='signin')
def stockOut(request):
    return render(request, 'stock/stockOut.html')


@login_required(login_url='signin')
def stockNew(request):
    if request.method == 'POST':
        type_id = request.POST.get('type_id')
        totalAmount = request.POST.get('totalAmount')
        stock = InventoryStock()
        type_instance = Type.objects.get(id=type_id)
        stock.type_id = type_instance
        stock.totalAmount = totalAmount

        stock.save()
        return redirect('stockList')
    types = Type.objects.all().order_by('id')
    context = {'types': types}
    return render(request, 'stock/stockNew.html', context)


@login_required(login_url='signin')
def stockList(request):
    stock = InventoryStock.objects.all().order_by('id')
    context = {'stocks': stock}
    return render(request, 'stock/stockList.html', context)


@login_required(login_url='signin')
def stockDelete(request, id):
    stock = get_object_or_404(InventoryStock, id=id)
    if request.method == 'POST':
        stock.delete()
        return redirect('stockList')
    context = {'stock': stock}
    return render(request, 'stock/stockDelete.html', context)


@login_required(login_url='signin')
def stockUpdate(request, id):
    stock = get_object_or_404(InventoryStock, id=id)
    if request.method == 'POST':
        type_id = request.POST.get('type_id')
        totalAmount = request.POST.get('totalAmount')
        type_instance = Type.objects.get(id=type_id)
        stock.type_id = type_instance
        stock.totalAmount = totalAmount
        stock.save()
        return redirect('stockList')
    types = Type.objects.all().order_by('id')
    context = {'stock': stock, 'types': types}
    return render(request, 'stock/stockUpdate.html', context)


@login_required(login_url='signin')
def typeNew(request):
    if request.method == 'POST':
        productName = request.POST.get('productName')
        rateReceive = request.POST.get('rateReceive')
        rateSend = request.POST.get('rateSend')
        type = Type()
        type.productName = productName
        type.rateReceive = rateReceive
        type.rateSend = rateSend
        type.save()
        return redirect('typeList')
    else:
        return render(request, 'type/typeNew.html')


@login_required(login_url='signin')
def typeList(request):
    type = Type.objects.all().order_by('id')
    context = {'types': type}
    return render(request, 'type/typeList.html', context)


@login_required(login_url='signin')
def typeDelete(request, id):
    type = get_object_or_404(Type, id=id)
    if request.method == 'POST':
        type.delete()
        return redirect('typeList')
    context = {'type': type}
    return render(request, 'type/typeDelete.html', context)


@login_required(login_url='signin')
def typeUpdate(request, id):
    type = get_object_or_404(Type, id=id)
    if request.method == 'POST':
        productName = request.POST.get('productName')
        rateReceive = request.POST.get('rateReceive')
        rateSend = request.POST.get('rateSend')
        type.productName = productName
        type.rateReceive = rateReceive
        type.rateSend = rateSend
        type.save()
        return redirect('typeList')
    context = {'type': type}
    return render(request, 'type/typeUpdate.html', context)


@login_required(login_url='signin')
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


@login_required(login_url='signin')
def cusList(request):
    customers = Customer.objects.all().order_by('id')
    context = {'customers': customers}
    return render(request, 'customer/cusList.html', context)


@login_required(login_url='signin')
def cusDelete(request, id):
    cus = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        cus.delete()
        return redirect('cusList')
    else:
        data = {'cus': cus}
        return render(request, 'customer/cusDelete.html', data)


@login_required(login_url='signin')
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


@login_required(login_url='signin')
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


@login_required(login_url='signin')
def empList(request):
    employees = Employee.objects.all().order_by('id')
    context = {'employees': employees}
    return render(request, 'employee/empList.html', context)


@login_required(login_url='signin')
def empDelete(request, id):
    emp = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        emp.delete()
        return redirect('empList')
    else:
        data = {'emp': emp}
        return render(request, 'employee/empDelete.html', data)


@login_required(login_url='signin')
def empUpdate(request, id):
    emp = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        username = request.POST['inputUsername']
        email = request.POST['inputEmail']
        fullname = request.POST['inputFullname']
        address = request.POST['inputAddress']
        tell = request.POST['inputTell']
        emp = Employee(id, username, email, fullname, address, tell)
        emp.save()
        return redirect('empList')
    else:
        data = {'emp': emp}
        return render(request, 'employee/empUpdate.html', data)
