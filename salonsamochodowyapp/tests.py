from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import ListCars

class ListCarsModelTest(TestCase):
    def setUp(self):
        # Create a simple image file
        image = SimpleUploadedFile(name='test_image.jpg', content=open(r"C:\Users\Programowanie\Desktop\Guzik Cwel\testowanie-dariusz-reimann\media_car\Polski_Fiat_126p_rocznik_1973.jpg", 'rb').read(), content_type='image/jpeg')

        # Create a ListCars object with the image
        self.car = ListCars.objects.create(
            carName='Test Car',
            carDescription='This is a test car.',
            carPrice=10000,
            carYear=2020,
            carImage=image
        )

    def test_image_field(self):
        # Try to access the image field
        try:
            image = self.car.carImage
            self.fail('Expected an Exception but none was raised.')
        except Exception as e:
            self.assertIsInstance(e, ValueError)  # Replace YourExpectedException with the exception you expect to be raised
