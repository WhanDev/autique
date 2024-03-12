from django.shortcuts import render
def home(request):
    return render(request, 'dasbord.html')
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
    return render(request, 'customer/cusNew.html')
def cusList(request):
    return render(request, 'customer/cusList.html')
def cusDelete(request):
    return render(request, 'customer/cusDelete.html')
def cusUpdate(request):
    return render(request, 'customer/cusUpdate.html')

def empNew(request):
    return render(request, 'employee/empNew.html')
def empList(request):
    return render(request, 'employee/empList.html')
def empDelete(request):
    return render(request, 'employee/empDelete.html')
def empUpdate(request):
    return render(request, 'employee/empUpdate.html')