from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.models import longProfile

# Create your   views here.
class views:
    def home(request):
        if redirect('home'):
            return redirect('home')
        return render(request, 'main/index.html')

    def settings(request):
        return render(request, 'main/settings.html')

    def register(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')
                return redirect('login')
        else:
            form = UserCreationForm()
        return render(request, 'main/register.html', {'form': form})

    def login_view(request):
        from django.contrib.auth import authenticate, login
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users:profile')
            else:
                messages.error(request, 'Invalid username or password.')
        return render(request, 'main/login.html')

    @login_required
    def logout_view(request):

        if request.user.is_authenticated:
            from django.contrib.auth import logout
            logout(request)
            return redirect('home')
        else:
            return redirect('home')