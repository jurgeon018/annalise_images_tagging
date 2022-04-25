from django.db import models


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(blank=False, null=False, auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(blank=False, null=False, auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Image(TimestampMixin):
    image = models.ImageField(blank=False, null=False)
    # metadata
    filename = models.CharField(max_length=255, blank=True, null=True)
    size = models.CharField(max_length=255, blank=True, null=True)
    height = models.CharField(max_length=255, blank=True, null=True)
    width = models.CharField(max_length=255, blank=True, null=True)
    format = models.CharField(max_length=255, blank=True, null=True)
    mode = models.CharField(max_length=255, blank=True, null=True)
    metadata_is_synced = models.BooleanField(default=False)
    last_synced_at = models.DateTimeField(blank=True, null=True)
    
    tags = models.ManyToManyField(to='images.Tag', through='images.ImageTag', related_name='images')

    def __str__(self):
        return f'Image #{self.id}'


class Tag(TimestampMixin):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}({self.pk})'


class ImageTag(TimestampMixin):
    image = models.ForeignKey(to='images.Image', on_delete=models.CASCADE)
    tag = models.ForeignKey(to='images.Tag',  on_delete=models.CASCADE)

    def __str__(self):
        return f'ImageTag #{self.id}; image:{self.image.pk}; tag:{self.tag.pk}'
