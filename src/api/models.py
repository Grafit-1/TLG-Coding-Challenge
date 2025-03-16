from django.db import models

# Create your models here.

from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class HolidaySchedule(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    destinations = models.ManyToManyField(Destination, through='ScheduleOrder')

    def __str__(self):
        return self.name

class ScheduleOrder(models.Model):
    holiday_schedule = models.ForeignKey(HolidaySchedule, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']
