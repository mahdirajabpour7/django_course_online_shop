# Generated by Django 4.0.2 on 2023-08-09 10:05

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_comment_datetime_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='datetime_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/product_cover/', verbose_name='Product_Image'),
        ),
    ]
