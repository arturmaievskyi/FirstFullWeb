from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your   views here.

def home(request):
    return render(request, 'main/index.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username, password=password)
                return redirect('profile')
            except User.DoesNotExist:
                messages.error(request, 'Invalid credentials')
    return  render(request, 'main/login.html')

def register(request):
    
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username and password and email:
            if User.objects.filter(username=username).exists():
                return render(request, 'main/register.html', {'error': 'Username taken'})
            
            User.objects.create(username=username, email=email, password=password)

    return render(request, 'main/register.html')

@login_required
def profile(request):
    return render(request, 'main/profile.html')

def settings(request):
    return render(request, 'main/settings.html')

@login_required
def logout_view(request):

    if request.user.is_authenticated:
        from django.contrib.auth import logout
        logout(request)
        return redirect('home')
    return redirect('home')
    