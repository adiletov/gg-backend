from django.db import models
from users.models import User
from .utils import dealer_image_upload_path

class Dealer(models.Model):
    user = models.ForeignKey(User, related_name='dealerships', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DealerImage(models.Model):
    dealer = models.ForeignKey(Dealer, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=dealer_image_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.dealer.name}"

