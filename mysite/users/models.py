from django.db import models

# Create your models here.
class longProfile(models.Model):
    short_profile = models.OneToOneField(
        'main.shortProfile', 
        on_delete=models.CASCADE,
        related_name='extended_profile'
    )

    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    username = models.CharField(max_length=150, unique=True)
    favourites_textes = models.ManyToManyField('textes.Text', related_name='favorited_by', blank=True)
    favourites_projects = models.ManyToManyField('projects.Project', related_name='favorited_by', blank=True)
    followed_users = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    following_users = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    