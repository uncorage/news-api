from rest_framework import serializers
from .models import *

# class JournalistSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=60)
#     last_name = serializers.CharField(max_length=60)
#     bio = serializers.CharField()

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    publication_date = serializers.CharField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.save()
        return instance