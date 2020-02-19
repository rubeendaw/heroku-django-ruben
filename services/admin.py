from django.contrib import admin
from .models import Service
from .models import Comment

admin.site.register(Service)
admin.site.register(Comment)