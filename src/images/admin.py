from django.contrib import admin
from images.models import Image, Tag, ImageTag


class ItemTagInline(admin.TabularInline):
    model = ImageTag
    autocomplete_fields = [
        'tag'
    ]
    extra = 0
    


class ImageAdmin(admin.ModelAdmin):
    inlines = [
        ItemTagInline
    ]
    list_per_page = 10
    list_filter = [
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
    list_display = [
        'id',
        'filename',
        'image',
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
    list_display_links = [
        'id',
        'filename',
    ]
    readonly_fields = [
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
    search_fields = [
        'filename',
    ]


class TagAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'description',
    ]
    list_display_links = [
        'id',
    ]
    list_editable = [
        'name',
        'description',
    ]
    list_filter = [
        'created_at',
        'updated_at',
    ]
    search_fields = [
        'name',
        'description'
    ]


admin.site.register(Image, ImageAdmin)
admin.site.register(Tag, TagAdmin)
