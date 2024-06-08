from django.urls import path, include
from .views import ClimatViewSet, ContinentViewSet, CountryViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'climat', ClimatViewSet)
router.register(r'continent', ContinentViewSet)
router.register(r'country', ContinentViewSet)


urlpatterns = [
    path('', include(router.urls))
]

