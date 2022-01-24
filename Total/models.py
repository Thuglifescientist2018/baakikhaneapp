from django.db import models

# Create your models here.


class Total(models.Model):
    total_price = models.FloatField(blank=False, null=True)
