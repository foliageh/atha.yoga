# Generated by Django 4.1.4 on 2022-12-29 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_alter_user_rate"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="register_confirm_token",
            field=models.CharField(
                blank=True,
                max_length=300,
                null=True,
                verbose_name="register confirm token",
            ),
        ),
    ]
