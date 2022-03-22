from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, LoginForm

# Create your views here.
# class Index(View):
#     def get(self, request):
#         return render(request, 'authentication/index.html')

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('dashboard')
        else:
            form = LoginForm()
    return render(request, 'authentication/index.html', {'form': form})

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form = RegisterForm()
            form.save()
            return redirect('login')
        else:
            form = RegisterForm()

    return render(request, 'authentication/register.html', {'form': form})

def dashboard(request):
    return render(request, 'authentication/dashboard.html')
