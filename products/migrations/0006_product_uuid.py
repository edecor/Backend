# Generated by Django 3.2.6 on 2021-09-03 05:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_alter_productimage_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
    ]
