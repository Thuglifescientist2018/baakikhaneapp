from django.db import models

# Create your models here.


class Total(models.Model):
    count = models.IntegerField(blank=False, null=False)
    total_price = models.FloatField(blank=False, null=True)
