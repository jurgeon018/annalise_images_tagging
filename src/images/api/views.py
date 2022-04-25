from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from images.api.serializers import ImageSerializer, TagSerializer
from images.models import Image, Tag


class ImageList(ListCreateAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class ImageDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class TagList(ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TagDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

