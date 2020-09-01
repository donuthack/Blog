from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Publication


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class MiniPublicationSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Publication
        fields = ['id', 'title', 'publication_date', 'author']


class PublicationSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Publication
        fields = '__all__'


class CreateOrUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        fields = '__all__'
