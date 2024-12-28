from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from object_storage.factory import S3ServiceFactory

from .models import Product


@receiver(post_save, sender=Product)
def upload_image_to_s3(sender, instance, created, **kwargs):
    if instance.image and created:
        endpoint = settings.MINIO_ENDPOINT
        bucket_name = settings.BUCKET_NAME
        access_key = settings.ACCESS_KEY
        secret_key = settings.SECRET_KEY

        s3_factory = S3ServiceFactory(endpoint, access_key, secret_key)
        s3_service = s3_factory.create_service(bucket_name)

        image_content = instance.image.read()
        image_name = instance.image.name.split("/")[-1]

        s3_service.upload_file_object("products/images/", image_name, image_content)

        instance.image.name = f"products/images/{image_name}"
        instance.save(update_fields=["image"])
