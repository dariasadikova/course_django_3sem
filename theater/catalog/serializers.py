from catalog.models import Play, Genre
from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name'] 

class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ['name', 'genre', 'director', 'datetime']


