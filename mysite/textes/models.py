from django.db import models

class Text(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content_per_chapter = models.IntegerField(default=10)
    chapters = models.IntegerField(default=1)
    views = models.IntegerField(default=0, editable=False)
    favorites = models.ManyToManyField('auth.User', related_name='favorite_texts', editable=False)
    favorites_count = models.IntegerField(default=0)
    authors = models.ManyToManyField('auth.User', related_name='authored_texts', editable=False)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.content:
            self.chapters = (len(self.content) - 1) // self.content_per_chapter + 1
        super().save(*args, **kwargs)

    def increment_views(self):
        self.views += 1
        self.save()

    