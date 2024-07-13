from rest_framework.routers import DefaultRouter
from django.urls import path, include
from core.views import MovieViewset


router = DefaultRouter()
router.register(r'movies', MovieViewset, basename='movies')

urlpatterns = [
    path('', include(router.urls))
]