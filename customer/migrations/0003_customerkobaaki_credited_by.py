# Generated by Django 4.0.1 on 2022-01-25 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customerkobaaki_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerkobaaki',
            name='credited_by',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
