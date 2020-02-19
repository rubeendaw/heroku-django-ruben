# from django.contrib.auth.models import User
from django.contrib import admin
# from rest_framework import routers, serializers, viewsets
from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.authentication.urls', namespace='authentication')),
    path('api-auth/', include('rest_framework.urls')),
    path('services/', include('services.urls')),
]
