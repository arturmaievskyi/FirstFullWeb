from django.contrib import admin
from .models import Text
# Register your models here.
admin.site.register(Text)

class TextAdmin(admin.ModelAdmin):
    readonly_fields = ('favorites_count', 'views', 'chapters', 'created_at', 'updated_at', 'content_per_chapter')
    fields = ('title', 'content', 'content_per_chapter', 'chapters', 'views', 'favorites_count', 'authors', 'created_at', 'updated_at')
