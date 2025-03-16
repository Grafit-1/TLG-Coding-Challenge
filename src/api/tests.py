from django.test import TestCase
from api.models import Destination
from api.utils import fetch_weather
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class DestinationModelTest(TestCase):
    def test_create_destination(self):
        destination = Destination.objects.create(
            name="Paris",
            latitude=48.8566,
            longitude=2.3522
        )
        self.assertEqual(destination.name, "Paris")
        self.assertEqual(destination.latitude, 48.8566)
        self.assertEqual(destination.longitude, 2.3522)

class DestinationAPITest(APITestCase):
    def setUp(self):
        self.destination = Destination.objects.create(
            name="Paris",
            latitude=48.8566,
            longitude=2.3522
        )
    
    def test_get_destinations_list(self):
        """Test retrieving a list of destinations"""
        url = reverse("destination-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_get_single_destination(self):
        """Test retrieving a single destination"""
        url = reverse("destination-detail", args=[self.destination.id])  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Paris")


class WeatherUtilsTest(TestCase):
    def test_fetch_weather(self):
        """Test fetching weather for a valid location"""
        latitude = 48.8566
        longitude = 2.3522
        weather_data = fetch_weather(latitude, longitude)

        self.assertIsInstance(weather_data, list) # returns list
        self.assertGreater(len(weather_data), 0) # list has content
        self.assertIn("temperature_2m_min", weather_data[0])  # Expected key in response