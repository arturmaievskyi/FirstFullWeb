from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profile_view(request):
    profilePicture = request.user.extended_profile.short_profile.profile_picture
    
    context = {
        'profilePicture': profilePicture
    }
    return render(request, 'users/profile.html', context)

@login_required
def profile_settings(request):
    return render(request, 'users/profile_settings.html')

@login_required
def change_password(request):
    return render(request, 'users/change_password.html')

@login_required
def delete_account(request):
    return render(request, 'users/delete_account.html')

@login_required
def notifications(request):
    return render(request, 'users/notifications.html')

@login_required
def followers(request):
    return render(request, 'users/followers.html')

@login_required
def following(request):
    return render(request, 'users/following.html')

@login_required
def friends(request):
    return render(request, 'users/friends.html')

@login_required
def userProjects(request):
    user_projects = request.user.projects.all()
    context = {
        'user_projects': user_projects
    }
    return render(request, 'users/projects.html', context)