from django.db import models
from datetime import datetime


# from compositefk.fields import CompositeForeignKey


class FlatType(models.Model):
    flat_type = models.CharField(max_length=20)
    flat_desc = models.TextField(blank=True)

    def __str__(self):
        return self.flat_type


# Create your models here.
class FlatTypeDetail(models.Model):
    flat_type = models.ForeignKey(FlatType, on_delete=models.DO_NOTHING)
    sqft = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    price = models.IntegerField(default=0)
    dining_hall = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    isometric_view = models.ImageField(upload_to='photos/%Y/%m/%d/')
    floor_plan = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        unique_together = (('flat_type', 'sqft'),)
        index_together = (('flat_type', 'sqft'),)
        #unique_together = [['driver', 'restaurant']]

    def __str__(self):
        return self.description

    '''class Meta:
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['first_name'], name='first_name_idx'),
        ]''''''

    # def __str__(self):
    # return "%s %s" % (self.flat_type, self.sqft)
    def __str__(self):
    # return self.flat_type_desc'''


class BlockType(models.Model):
    block_name = models.CharField(max_length=100)
    floor_num_start = models.IntegerField()
    floor_num_end = models.IntegerField()

    def __str__(self):
        return self.block_name


class FloorRangeAllocation(models.Model):
    block_name = models.ForeignKey(BlockType, on_delete=models.DO_NOTHING)
    floor_number = models.IntegerField()
    def __int__(self):
        return self.floor_number


class UnitFlat(models.Model):
    title = models.CharField(max_length=20)  # House Number
    unit_flat_type = models.ForeignKey(FlatTypeDetail, on_delete=models.DO_NOTHING)
    block_name = models.ForeignKey(BlockType, on_delete=models.DO_NOTHING)
    floor_number = models.ForeignKey(FloorRangeAllocation, on_delete=models.DO_NOTHING)
    is_available = models.BooleanField(default=True)
    Facing = models.CharField(max_length=100)
    description= models.TextField(blank=True)
    car_parking = models.BooleanField(default=True)

class BlockBaseImage(models.Model):
    block_flat_type = models.ForeignKey(FlatTypeDetail, on_delete=models.DO_NOTHING)
    #block_sqft = models.ForeignKey(FlatTypeDetail, to_field="sqft", db_column="sqft",on_delete=models.DO_NOTHING)
    block_name = models.ForeignKey(BlockType, on_delete=models.DO_NOTHING)
    Number_of_flats = models.IntegerField()




class Carousel(models.Model):
    slide_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    slide_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    slide_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    slide_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    slide_photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    slide_photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)


'''class BlockTypes(models.Model):
    block_name = models.CharField(max_length=100)
    floor_num_start = models.IntegerField()
    floor_num_end = models.IntegerField()


class FloorRangeAllocation(models.Model):
    block_name = models.ForeignKey(BlockTypes, on_delete=models.DO_NOTHING)
    floor_number = models.IntegerField()


class BlockBaseImage(models.Model):
    block_flat_type = models.ForeignKey(FlatTypeDetails, on_delete=models.DO_NOTHING)
    block_flat_sqft = models.ForeignKey(FlatTypeDetails, on_delete=models.DO_NOTHING)
    block_name = models.ForeignKey(BlockTypes, on_delete=models.DO_NOTHING)
    Number_of_flats = models.IntegerField()


class UnitFlats(models.Model):
    title = models.CharField(max_length=20)  # House Number
    unit_flat_type = models.ForeignKey(FlatTypeDetails, on_delete=models.DO_NOTHING)
    unit_sqft= models.ForeignKey(FlatTypeDetails, on_delete=models.DO_NOTHING)
    block_name = models.ForeignKey(BlockTypes, on_delete=models.DO_NOTHING)
    floor_number = models.ForeignKey(FloorRangeAllocation, on_delete=models.DO_NOTHING)
    is_available = models.BooleanField(default=True)
    Facing = models.CharField(max_length=100)
    description= models.TextField(blank=True)
    car_parking = models.BooleanField(default=True)'''

# def __str__(self):
#   return self.flat_type
