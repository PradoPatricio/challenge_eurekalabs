# Generated by Django 4.2 on 2023-04-14 19:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="apiuser",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="apiuser",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
    ]
