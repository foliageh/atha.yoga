# Generated by Django 4.1.4 on 2022-12-29 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0007_alter_course_rate"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="lesson",
            options={
                "ordering": ("id",),
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
            },
        ),
    ]
