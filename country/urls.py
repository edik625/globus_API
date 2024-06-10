from django.urls import path, include
from .views import ClimatViewSet, ContinentViewSet, CountryViewSet #gets
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'climat', ClimatViewSet)
router.register(r'continent', ContinentViewSet)
router.register(r'country', CountryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('country/<str:name>',  gets)
]

