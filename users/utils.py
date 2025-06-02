def dealer_image_upload_path(instance, filename):
    return f"dealers/{instance.dealer.id}/{filename}"