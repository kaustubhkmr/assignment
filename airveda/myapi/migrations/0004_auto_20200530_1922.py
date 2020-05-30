# Generated by Django 3.0.6 on 2020-05-30 19:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_auto_20200530_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperaturereading',
            name='reading',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(-50), django.core.validators.MaxValueValidator(100)]),
        ),
    ]