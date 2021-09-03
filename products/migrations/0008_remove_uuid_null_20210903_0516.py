# Generated by Django 3.2.6 on 2021-09-03 05:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0007_populate_uuid_values_20210903_0515"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
