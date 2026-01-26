from django.shortcuts import render

# Create your views here.

def home(request):
    data = {
        "MyTitle": "Main Page",
        "Content": "Welcome to the Main Page",
        "About": "This is the home page of our website."
        }

    return render(request, 'main/index.html', context=data)


def login_view(request):
    return  render(request, 'main/login.html')

def register(request):
    return render(request, 'main/register.html')

def profile(request):
    return render(request, 'main/profile.html')

def settings(request):
    return render(request, 'main/settings.html')



