from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    Followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    followers_count = models.IntegerField(default=0)
    textes_count = models.IntegerField(default=0)
    textes = models.ManyToManyField('Text', related_name='authors', blank=True)
    projects_count = models.IntegerField(default=0)
    projects = models.ManyToManyField('projects.Projects', related_name='contributors', blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"