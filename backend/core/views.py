from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions, status
from rest_framework.response import Response
from core.models import Movie
from django.db.models import Q
from core.serializers import MovieSerializer, MovieBarChartSerializer, MovieLineChartSerializer, MovieChartSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
# Create your views here.


@extend_schema(
    parameters=[
        OpenApiParameter(name='year', description='select the year', type=str, enum=[date for date in range(1932, 2023+1)]),
    ]
)
class MovieViewset(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny,]



    @action(detail=False, methods=['GET'])
    def bar_chart(self, request):
        year = request.GET.get("year", "")
        queryset = self.get_queryset().filter(year=year).only('gross','movie').order_by("-gross")[:5]
        serializer = MovieBarChartSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def line_chart(self, request):
        queryset = self.get_queryset().order_by('-votes')[:5]
        serializer = MovieLineChartSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def chart(self, request):
        year = request.GET.get("year", "")
        queryset = self.get_queryset().filter(year=year).order_by("-rating").only('rating','movie')[:10]
        serializer = MovieChartSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)