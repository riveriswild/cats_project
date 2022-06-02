from rest_framework import serializers
from .models import Cat


class CatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ('id', 'name', 'breed', 'sex')


class CatDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ('id', 'name', 'description', 'breed', 'color', 'eye_color', 'size', 'sex', 'hair', 'dateCreation')




