# Generated by Django 3.2.7 on 2021-10-06 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_material_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]