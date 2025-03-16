# serializers.py
from rest_framework import serializers
from .models import Destination, HolidaySchedule, ScheduleOrder
import requests
from .utils import fetch_weather

class DestinationSerializer(serializers.ModelSerializer):
    weather = serializers.SerializerMethodField()

    class Meta:
        model = Destination
        fields = "__all__"

    def get_weather(self, obj):
        return fetch_weather(obj.latitude, obj.longitude)

class ScheduleOrderSerializer(serializers.ModelSerializer):
    destination = DestinationSerializer()

    class Meta:
        model = ScheduleOrder
        fields = ["destination", "order"]

class HolidayScheduleSerializer(serializers.ModelSerializer):
    schedule_orders = ScheduleOrderSerializer(source='scheduleorder_set', many=True, read_only=True)

    class Meta:
        model = HolidaySchedule
        fields = ["id", "name", "created_at", "schedule_orders"]