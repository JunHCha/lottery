# Generated by Django 3.1.2 on 2020-10-05 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotteryapp', '0006_auto_20201005_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemrequest',
            name='limit_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='itemshare',
            name='limit_time',
            field=models.CharField(max_length=100),
        ),
    ]
