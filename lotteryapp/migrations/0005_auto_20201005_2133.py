# Generated by Django 3.1.2 on 2020-10-05 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotteryapp', '0004_auto_20201005_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemrequest',
            name='remain',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='itemshare',
            name='remain',
            field=models.IntegerField(default=0),
        ),
    ]