from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin_url')
    temp = 'auth_app/signup.html'
    context = {'form':form}
    return render(request, temp, context)

def login_view(request):

    temp = 'auth_app/login.html'
    context = {}

    if request.method == 'POST':
        u = request.POST.get('un')
        p = request.POST.get('pw')

        user = authenticate(username = u, password = p)

        if user is not None:
            login (request, user)
            return redirect('add_url')
    return render (request, temp, context)

    

def logout_view(request):
    logout(request)
    return redirect('signin_url')

