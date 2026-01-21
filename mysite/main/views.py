from django.shortcuts import render


# Create your views here.

def home(request):
    data = {"Title": "Main Page"}
    return render(request, 'index.html', context=data)


def login_view(request):
    return  render(request, 'main/login.html')

def register(request):
    return render(request, 'main/register.html')

def profile(request):
    return render(request, 'main/profile.html')

def settings(request):
    return render(request, 'main/settings.html')



