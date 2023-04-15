# Generated by Django 4.0.7 on 2023-04-14 10:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_DS', '0002_relevancy_ds_conciseness_ds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_ds',
            name='clean_SCORE',
            field=models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)], verbose_name='clean SCORE'),
        ),
    ]