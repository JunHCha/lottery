# Generated by Django 3.1.2 on 2020-10-12 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_profile_address_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='profile',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
    ]