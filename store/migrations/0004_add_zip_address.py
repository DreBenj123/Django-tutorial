# Generated by Django 4.1.7 on 2023-03-13 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_add_slug_to_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="zip",
            field=models.TextField(default=False),
        ),
    ]
