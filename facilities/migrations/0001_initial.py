# Generated by Django 4.2.4 on 2023-08-20 04:45

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HealthFacilites",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=80)),
                ("healthcare", models.CharField(max_length=167)),
                ("amenity", models.CharField(max_length=80)),
                ("operatorty", models.CharField(max_length=80)),
                ("geom", django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
