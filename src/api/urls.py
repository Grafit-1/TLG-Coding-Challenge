from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import DestinationViewSet, HolidayScheduleViewSet

router = DefaultRouter()
router.register(r"destinations", DestinationViewSet)
router.register(r"holiday_schedules", HolidayScheduleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]