import os

def car_image_upload_path(instance, filename):
    brand_name = instance.car.brand.name if instance.car.brand else 'unknown_brand'
    safe_brand = brand_name.lower().replace(' ', '_')
    return os.path.join('cars', safe_brand, filename)