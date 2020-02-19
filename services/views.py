from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Service, Comment
from services.serializers import ServiceSerializer, CommentSerializer
from rest_framework.response import Response

class ServiceViewSetAdmin(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class CommentViewSetAdmin(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

class CommentsListAPIView(generics.ListCreateAPIView):
    lookup_field = 'comment__service'
    lookup_url_kwarg = 'service_id'
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def filter_queryset(self, queryset):
        filters = self.kwargs[self.lookup_url_kwarg]
        return queryset.filter(services=filters)

    def create(self, request, service_id=None):
        filters = self.kwargs[self.lookup_url_kwarg]
        data = request.data.get('comment', {})
        context = {'profile': request.user.profile}
        
        try:
            context['services'] = Service.objects.get(id=service_id)
        except Service.DoesNotExist:
            raise NotFound('No existe el servicio')
    
        serializer = self.serializer_class(data=data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)