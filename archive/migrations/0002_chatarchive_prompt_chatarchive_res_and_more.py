# Generated by Django 4.2.6 on 2023-10-28 18:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("archive", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chatarchive",
            name="prompt",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="chatarchive",
            name="res",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="chatarchive",
            name="body",
            field=models.TextField(max_length=100),
        ),
    ]