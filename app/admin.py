from django.contrib import admin
from .models import CustomUser, Blog, Comment, Like
# Register your models here.

admin.site.register(Blog)
admin.site.register(CustomUser)
admin.site.register(Comment)
admin.site.register(Like)