# Generated by Django 3.2.7 on 2021-10-09 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_auto_20211009_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='brand',
        ),
        migrations.AddField(
            model_name='material',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products_material_related', related_query_name='products_materials', to='products.brand'),
        ),
        migrations.AlterField(
            model_name='material',
            name='supplier',
            field=models.ManyToManyField(blank=True, related_name='products_material_related', related_query_name='products_materials', to='products.Supplier'),
        ),
    ]