from rest_framework.routers import DefaultRouter
from .views import RoomViewSet

router = DefaultRouter()
router.register(r'Room', RoomViewSet, basename='Room')

urlpatterns = router.urls