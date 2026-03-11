from django.contrib import admin
from .models import User, shortProfile

# Register your models here.
admin.site.register(User)
admin.site.register(shortProfile)