from django.contrib import admin

# Register your models here.
from .models import Restaurant, Comment

admin.site.register(Restaurant)
admin.site.register(Comment) 