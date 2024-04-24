from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from salonsamochodowyapp.models import ListCars
from django.test import TestCase
from django.urls import reverse

class CarImageTest(TestCase):
    def setUp(self):
        self.client = Client()
        with open("./salonsamochodowyapp/test.jpg", 'rb') as i:
            self.carImage = SimpleUploadedFile(name='test_image.jpg', content=i.read(), content_type='image/jpeg')
        self.car = ListCars.objects.create(carImage=self.carImage, carName="Test", carDescription="Test description", carPrice=2137, carYear=2023)

    def test_image_display(self):
        response = self.client.get("/media_car/" + str(self.car.carImage))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'image/jpeg')

    def test_car_creation(self):
        car = ListCars.objects.get(carName="Test")
        self.assertEqual(car.carPrice, 2137)
        self.assertEqual(car.carYear, 2023)

    def test_description(self):
        car = ListCars.objects.get(carName="Test")
        car.carDescription = "New test description"
        car.save()
        self.assertEqual(car.carDescription, "New test description")

    def test_string_representation(self):
        car = ListCars.objects.get(carName="Test")
        self.assertEqual(car.string_representation(),
                         "Test from 2023 for only 2137")

    def test_get_absolute_url(self):
        car = ListCars.objects.get(carName="Test")
        self.assertEqual(car.get_absolute_url(), reverse('car-detail', kwargs={
            'pk': car.pk}))
    def test_available_default(self):
        car = ListCars.objects.get(carName="Test")
        self.assertTrue(car.carAvailable)

    def test_reserve_method(self):
        car = ListCars.objects.get(carName="Test")
        car.reserve()
        self.assertFalse(car.carAvailable)
    def test_is_new_release(self):
        car = ListCars.objects.get(carName="Test")
        self.assertTrue(car.is_new())