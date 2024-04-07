from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Employee
from . forms import EmployeeForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='signin_url')
def add_data(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    temp = 'app/add.html'
    context = {'form':form}
    return render(request, temp, context)

@login_required(login_url='signin_url')
def show_data(request):
    obj = Employee.objects.all()
    temp = 'app/show.html'
    context = {'form':obj}
    return render(request, temp, context)

def update_data(request,pk):
    obj = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=obj)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect ('show_url')
    temp = 'app/add.html'
    context = {'form':form}
    return render(request,temp, context)

def delete_data(request, pk):
    obj = Employee.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect ('show_url')
    temp = 'app/delete.html'
    context = {'obj':obj}
    return render(request, temp, context)