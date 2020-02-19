from rest_framework import serializers
from apps.profiles.serializers import ProfileSerializer
from .models import Service
from .models import Comment

class ServiceSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)

    class Meta:
        model = Service
        fields = ('id', 'slug', 'name_service', 'type_service', 'price')


class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    services = ServiceSerializer(many=False, read_only=True)
    body = serializers.CharField(max_length=255)

    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Comment
        fields = ('id', 'profile', 'services', 'body', 'createdAt', 'updatedAt')

    def create(self, validated_data):
        services = self.context['services']
        profile = self.context['profile']

        return Comment.objects.create(
            services=services, profile=profile, **validated_data
        )

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()