from django.db import models

# Create your models here.
class Projects(models.Model):
    Title = models.CharField(max_length=200)
    Short_Description = models.CharField(max_length=500)
    Description = models.TextField()
    Image = models.ImageField(upload_to='project_images/')
    Is_Public = models.BooleanField(default=True)
    Is_Completed = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    Favorites = models.ManyToManyField('auth.User', related_name='favorite_projects', blank=True)
    favorites_count = models.IntegerField(default=0)
    

    def __str__(self):
        return self.Title