from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from PIL import Image as pilImage
from datetime import datetime
from images.models import Image


def sync_metadata(
    image: Image
) -> None:
    path = image.image.path
    image_file = pilImage.open(path)
    image.filename = image_file.filename
    image.size = image_file.size
    image.height = image_file.height
    image.width = image_file.width
    image.format = image_file.format
    image.mode = image_file.mode
    image.last_synced_at = datetime.now()


@receiver(pre_save, sender=Image, dispatch_uid="pre_save_update_image_metadata")
def pre_save_update_image_metadata(sender, instance, **kwargs) -> None:
    try:
        if instance.pk:
            old_image = Image.objects.get(pk=instance.pk)

            if instance.image != old_image.image:
                sync_metadata(image=instance)
                instance.metadata_is_synced = False
    except FileNotFoundError as e:
        pass


@receiver(post_save, sender=Image, dispatch_uid="post_save_update_image_metadata")
def post_save_update_image_metadata(sender, instance, **kwargs) -> None:
    if not instance.metadata_is_synced:
        sync_metadata(image=instance)
        instance.metadata_is_synced = True
        instance.save()
