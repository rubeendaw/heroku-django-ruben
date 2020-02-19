from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSetAdmin, CommentViewSetAdmin, CommentsListAPIView
from django.conf.urls import url, include

router = DefaultRouter()
router.register('services', ServiceViewSetAdmin)
router.register('comments', CommentViewSetAdmin)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^(?P<service_id>[0-9a-zA-Z_-]+)/comments', CommentsListAPIView.as_view()),
]