# Generated by Django 4.2.6 on 2023-10-29 13:29

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ChatArchive",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid1,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("body", models.TextField(max_length=100)),
                ("prompt", models.TextField(blank=True)),
                ("res", models.TextField(blank=True)),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
