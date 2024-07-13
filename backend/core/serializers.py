from rest_framework import serializers
from core.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieBarChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['gross', 'movie', 'year']


class MovieLineChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['votes', 'movie', 'year']


class MovieChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['rating', 'movie', 'year']