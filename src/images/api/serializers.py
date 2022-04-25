from rest_framework.serializers import ModelSerializer
from images.models import Image, Tag


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        exclude = []


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        exclude = []
