from django.contrib import admin
from .models import FlatType,  Carousel, BlockType, \
    FloorRangeAllocation, FlatTypeDetail, BlockBaseImage, UnitFlat

class ListingFlatType(admin.ModelAdmin):
    list_display = ('id', 'flat_type', 'flat_desc')
    list_display_links = ('id', 'flat_type')
    #search_fields = ('flat_type',)
    list_per_page = 10


class ListingFlatTypeDetail(admin.ModelAdmin):
    list_display = ( 'id','flat_type_id','description', 'sqft', 'bedrooms', 'bathrooms', 'dining_hall')
    list_display_links = ('flat_type_id', 'sqft')
    list_editable = ('dining_hall',)
    #search_fields = ('flat_type_id', 'sqft')
    list_per_page = 10

class ListingBlockType(admin.ModelAdmin):
    list_display = ('id', 'block_name', 'floor_num_start','floor_num_end')
    list_display_links = ('id', 'block_name')
    list_per_page = 10

class ListingFloorRangeAllocation(admin.ModelAdmin):
    list_display = ('id', 'block_name', 'floor_number')
    list_display_links = ('id', 'block_name')
    list_per_page = 10

class ListingFloorRangeAllocation(admin.ModelAdmin):
    list_display = ('id', 'block_name', 'floor_number')
    list_display_links = ('id', 'block_name')
    list_per_page = 10

class ListingBlockBaseImage(admin.ModelAdmin):
    list_display = ('id', 'block_flat_type', 'block_name','Number_of_flats')
    list_display_links = ('id', 'block_flat_type','block_name')
    list_per_page = 10

class ListingUnitFlats(admin.ModelAdmin):
    list_display = ('id', 'title', 'unit_flat_type','block_name', 'floor_number','is_available','Facing')
    list_display_links = ('id', 'title')
    list_per_page = 10

# Register your models here
admin.site.register(FlatType,ListingFlatType)
admin.site.register(FlatTypeDetail,ListingFlatTypeDetail)
admin.site.register(Carousel)
admin.site.register(BlockType,ListingBlockType)
admin.site.register(FloorRangeAllocation,ListingFloorRangeAllocation)
admin.site.register(UnitFlat,ListingUnitFlats)
admin.site.register(BlockBaseImage,ListingBlockBaseImage)
