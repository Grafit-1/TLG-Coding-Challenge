from rest_framework import viewsets
from .models import Destination, HolidaySchedule
from .serializers import DestinationSerializer, HolidayScheduleSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class HolidayScheduleViewSet(viewsets.ModelViewSet):
    queryset = HolidaySchedule.objects.all()
    serializer_class = HolidayScheduleSerializer