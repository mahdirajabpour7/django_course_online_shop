# Generated by Django 4.0.2 on 2023-08-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_products_datetime_modified_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='short_description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]