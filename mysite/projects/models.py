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
    authors = models.ManyToManyField('auth.User', related_name='authored_projects', blank=True)
        

    def __str__(self):
        return self.Title
    
    def author_save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.favorites_count = self.Favorites.count()
        super().save(update_fields=['favorites_count'])

    def increment_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def add_favorite(self, user):
        self.Favorites.add(user)
        self.save(update_fields=['favorites_count'])

    def remove_favorite(self, user):
        self.Favorites.remove(user)
        self.save(update_fields=['favorites_count'])

