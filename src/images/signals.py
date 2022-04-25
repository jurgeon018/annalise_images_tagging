from django.db.models.signals import pre_save
from django.dispatch import receiver
from PIL import Image as pilImage
from datetime import datetime
from images.models import Image


@receiver(pre_save, sender=Image, dispatch_uid="update_image_metadata")
def update_image_metadata(sender, instance, **kwargs):
    print('kwargs', kwargs)
    image = instance
    try:
        path = image.image.path
        image_file = pilImage.open(path)
        image.filename = image_file.filename
        image.size = image_file.size
        image.height = image_file.height
        image.width = image_file.width
        image.format = image_file.format
        image.mode = image_file.mode
        metadata_is_synced = True
    except Exception as e:
        print(e)
        metadata_is_synced = False
    image.metadata_is_synced = metadata_is_synced
    image.last_synced_at = datetime.now()
