# Generated by Django 4.0.2 on 2023-08-08 04:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_comment_managers_products_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
