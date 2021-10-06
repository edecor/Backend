# Generated by Django 3.2.7 on 2021-10-06 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0015_temp_dummy_model"),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="productimage",
            name="content_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="productimage",
            name="object_id",
            field=models.PositiveIntegerField(null=True),
        ),
    ]
