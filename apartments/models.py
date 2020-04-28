from django.db import models
from datetime import datetime


# Create your models here.
class FlatType(models.Model):
    # realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    flat_type = models.CharField(max_length=20)
    sqft = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    price = models.IntegerField()
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
    list_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.flat_type


class Carousel(models.Model):

    slide_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    slide_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    slide_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    slide_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    slide_photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    slide_photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    #def __str__(self):
    #   return self.flat_type
