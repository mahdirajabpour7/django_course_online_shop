# Generated by Django 4.0.2 on 2023-08-11 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='userv',
            new_name='user',
        ),
    ]
