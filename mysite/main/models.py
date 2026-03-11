from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
class shortProfile(models.Model):
    User = models.OneToOneField(
        'main.User', 
        on_delete=models.CASCADE,
        related_name='extended_profile'
    )
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
