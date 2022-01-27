from django.db import models
from nepali_datetime_field.models import NepaliDateField
from cloudinary.models import CloudinaryField
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL


class CustomerKoBaaki(models.Model):
    user = models.ForeignKey(User, default=1, null=True,
                             on_delete=models.SET_NULL)
    sold_product = models.CharField(max_length=255, blank=False, null=True)
    product_image = CloudinaryField("image", null=True, blank=True)
    credited_by = models.CharField(blank=False, null=False, max_length=255)
    product_price = models.FloatField(
        blank=False, null=True)
    miti = NepaliDateField(null=True, blank=True)

    def __str__(self):
        return self.sold_product
