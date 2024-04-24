from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta
from datetime import date

# Create your models here.
class ListCars(models.Model):
    carName = models.CharField(max_length=255)
    carDescription = models.TextField(default="")
    carPrice = models.PositiveSmallIntegerField(default=1)
    carYear = models.PositiveSmallIntegerField(default=2000)
    carImage = models.ImageField(upload_to="",blank=True,null=True)
    carAvailable = models.BooleanField(default=True)

    def __str__(self):
        return self.carName

    def string_representation(self):
        return f"{self.carName} from {self.carYear} for only {self.carPrice}"

    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'pk': self.pk})

    def reserve(self):
        self.carAvailable = False
        self.save()

    def is_new(self):
        return (datetime.now().year - self.carYear) <= 2