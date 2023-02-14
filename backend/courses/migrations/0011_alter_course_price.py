# Generated by Django 4.1.6 on 2023-02-14 19:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0010_alter_ticket_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="price",
            field=models.FloatField(
                null=True,
                validators=[django.core.validators.MinValueValidator(limit_value=0)],
                verbose_name="Цена",
            ),
        ),
    ]