from django.shortcuts import render
from django.http import JsonResponse
from django.http.request import HttpRequest

# Create your views here.

def home(request):
    if request.method == 'GET':
        data = {
            'message': 'Hello from React!'
        }
        return JsonResponse(data)
    
    else:
        return render(request, 'main/home.html')

def login_view(request):
    return  render(request, 'main/login.html')

def register(request):
    return render(request, 'main/register.html')


def profile(request):
    return render(request, 'main/profile.html')

def settings(request):
    return render(request, 'main/settings.html')



