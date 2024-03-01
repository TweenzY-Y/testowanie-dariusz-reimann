from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from salonsamochodowyapp.models import ListCars
import os

class CarImageTest(TestCase):
    def setUp(self):
        self.client = Client()
        with open("./salonsamochodowyapp/test.jpg", 'rb') as i:
            self.carImage = SimpleUploadedFile(name='test_image.jpg', content=i.read(), content_type='image/jpeg')
        self.car = ListCars.objects.create(carImage=self.carImage, carName="Test", carDescription="Test description", carPrice=2000, carYear=2000)

    def test_image_display(self):
        response = self.client.get("/media_car/" + str(self.car.carImage))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'image/jpeg')