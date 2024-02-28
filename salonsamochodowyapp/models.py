from django.db import models

# Create your models here.
class ListCars(models.Model):
    carName = models.CharField(max_length=255)
    carDescription = models.TextField(default="")
    carPrice = models.PositiveSmallIntegerField(default=1)
    carYear = models.PositiveSmallIntegerField(default=2000)
    carImage = models.ImageField(upload_to="media_car",blank=True,null=True)

    def __str__(self):
        return self.carName