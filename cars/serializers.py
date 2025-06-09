from rest_framework import serializers
from .models import Car, Brand, Model, VehicleType, Color, CarImage
from dealers.models import Dealer
from dealers.serializers import DealerShortSerializer

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
    model_id = serializers.PrimaryKeyRelatedField(
        queryset=Model.objects.all(), source='model', write_only=True)
    vehicle_type_id = serializers.PrimaryKeyRelatedField(
        queryset=VehicleType.objects.all(), source='vehicle_type', write_only=True)
    dealer_id = serializers.PrimaryKeyRelatedField(
        queryset=Dealer.objects.all(), source='dealer', required=False, allow_null=True, write_only=True)
    brand = serializers.CharField(source='brand.name', read_only=True)
    model = serializers.CharField(source='model.name', read_only=True)
    images = CarImageSerializer(many=True, read_only=True)
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )
    images_urls = serializers.SerializerMethodField(read_only=True)
    dealer = DealerShortSerializer(read_only=True)

    class Meta:
        model = Car
        fields = [
            'id','dealer', 'price','model_id','vehicle_type_id','dealer_id',
            'brand', 'model',
            'images','year', 'created_at',
            'images_urls'
        ]
        read_only_fields = ('id', 'created_at', 'owner','brand','dealer')
        
    def get_images_urls(self, obj):
        return [image.image.url for image in obj.images.all()]
    
    def create(self, validated_data):
        images = validated_data.pop('images', [])
        model_obj = validated_data.pop('model')
        dealer_obj = validated_data.pop('dealer', None)
        user = self.context['request'].user
        brand_obj = model_obj.brand
        car = Car.objects.create(
            owner=user,
            brand=brand_obj,
            dealer=dealer_obj,
            model=model_obj,
            **validated_data
        )
        for image in images:
            CarImage.objects.create(car=car, image=image)
        return car