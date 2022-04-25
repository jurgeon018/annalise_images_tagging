from rest_framework.serializers import ModelSerializer, SerializerMethodField
from images.models import Image, Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        exclude = []


class ImageSerializer(ModelSerializer):
    tags_list = SerializerMethodField()

    def get_tags_list(self, obj):
        return TagSerializer(obj.tags.all(), many=True).data

    class Meta:
        model = Image
        exclude = []
        read_only_fields = [
            'id',
            'filename',
            'size',
            'height',
            'width',
            'format',
            'mode',    
            'metadata_is_synced',
            'last_synced_at',        
            'created_at',
            'updated_at',                   
        ]
