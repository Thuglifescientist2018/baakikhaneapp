
from enum import auto
from django.db import models
from nepali_datetime_field.models import NepaliDateField
from cloudinary.models import CloudinaryField

# Create your models here.


class CustomerKoBaaki(models.Model):
    sold_product = models.CharField(max_length=255, blank=False, null=True)
    product_image = CloudinaryField("image")
    credited_by = models.CharField(blank=False, null=False, max_length=255)
    product_price = models.FloatField(
        blank=False, null=True)
    miti = NepaliDateField(null=True, blank=True)

    def __str__(self):
        return self.sold_product
