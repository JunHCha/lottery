# Generated by Django 3.1.2 on 2020-10-09 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='010-0000-0000', max_length=20),
            preserve_default=False,
        ),
    ]