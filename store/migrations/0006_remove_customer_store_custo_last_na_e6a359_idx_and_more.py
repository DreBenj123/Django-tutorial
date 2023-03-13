# Generated by Django 4.1.7 on 2023-03-13 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_customer_store_custo_last_na_e6a359_idx_and_more"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="customer",
            name="store_custo_last_na_e6a359_idx",
        ),
        migrations.RenameField(
            model_name="customer",
            old_name="first_name",
            new_name="given_name",
        ),
        migrations.AlterModelTable(
            name="customer",
            table=None,
        ),
    ]
