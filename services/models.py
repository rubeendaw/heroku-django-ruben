# import datetime

from django.db import models
from apps.profiles.models import Profile
from apps.core.models import TimestampedModel 
# from django.utils import timezone

class Service(models.Model):
    slug = models.SlugField(db_index=True, max_length=500, unique=True)
    name_service = models.CharField(max_length=200)
    type_service = models.CharField(max_length=200)
    price = models.FloatField(max_length=7)

    def __str__(self):
        return self.name_service

class Comment(TimestampedModel):
    body = models.TextField()

    services = models.ForeignKey(
        Service, related_name='comments', on_delete=models.CASCADE
    )

    profile = models.ForeignKey(
        Profile, related_name='comments', on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.body