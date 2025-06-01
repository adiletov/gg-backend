from django.db import models
from users.models import User
from .utils import car_image_upload_path

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="models")
    name=models.CharField(max_length=100)
    start_year = models.PositiveIntegerField(null=True, blank=True)
    end_year = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('brand', 'name')

    def __str__(self):
        return self.name

class VehicleType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    mileage = models.PositiveIntegerField(help_text='Пробег в километрах')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    vin = models.CharField(max_length=17, unique=True, verbose_name='VIN', blank=True, null=True)
    year = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.brand.name} {self.model.name}'

class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=car_image_upload_path)
    def __str__(self):
        return f"Image for {self.car.brand.name} {self.car.model}"