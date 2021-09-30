# Generated by Django 3.2.7 on 2021-09-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_additional_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='is_description_image',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, help_text='To add images, Add description images through the form below first and then insert the url of the image here'),
        ),
    ]
