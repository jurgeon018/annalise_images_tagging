from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from images.api.serializers import ImageSerializer, TagSerializer
from images.models import Image, Tag
from images.api.paginators import StandardPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class ImageList(ListCreateAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    pagination_class = StandardPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'created_at':['gte', 'lte', 'exact', 'gt', 'lt'],
        'updated_at':['gte', 'lte', 'exact', 'gt', 'lt'],
        'last_synced_at':['gte', 'lte', 'exact', 'gt', 'lt'],
        'height':['exact'],
        'width':['exact'],
        'format':['exact'],
        'mode':['exact'],
        'metadata_is_synced':['exact'],
    }

class ImageDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class TagList(ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    pagination_class = StandardPageNumberPagination


class TagDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

