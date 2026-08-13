from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import HotelViewSet


router = DefaultRouter()

router.register("Hotel", HotelViewSet)


urlpatterns = [
    path("", include(router.urls)),
]