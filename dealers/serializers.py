from rest_framework import serializers
from .models import DealerImage, Dealer

class DealerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerImage
        fields = ['id', 'image']

class DealerSerializer(serializers.ModelSerializer):
    images = DealerImageSerializer(many=True, read_only=True)
    class Meta:
        model = Dealer
        fields = ['id', 'name', 'address', 'created_at', 'images']

class DealerShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ['id', 'name']