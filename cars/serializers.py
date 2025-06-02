from rest_framework import serializers
from .models import Car, Brand, Model, VehicleType, Color, CarImage
from users.serializers import UserSerializer

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'image']

class ModelSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name', read_only=True)
    class Meta:
        model = Model
        fields = ['id', 'name', 'brand', 'start_year', 'end_year','image']

class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ['id', 'name']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name']

class CarImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = CarImage
        fields = ['image_url']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


class CarSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    brand = serializers.CharField(source='brand.name', read_only=True)
    model = serializers.CharField(source='model.name', read_only=True)
    images = CarImageSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = [
            'id','owner', 'price',
            'brand', 'model',
            'images','year', 'created_at'
        ]
        read_only_fields = ('id', 'created_at', 'owner', 'year')