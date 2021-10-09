# Generated by Django 3.2.7 on 2021-10-09 15:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_decorationsproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='FabricTextileProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=400)),
                ('slug', models.SlugField(help_text='URL, will appear after you save for the first time', max_length=200, unique=True)),
                ('description', models.TextField(blank=True, help_text='To add images, Add description images through the form below first and then insert the url of the image here')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('additional_fields', models.JSONField(blank=True, help_text="To add extra fields, you can write a json. Delete the 'null' and start writing!", null=True)),
                ('place_of_origin', models.CharField(blank=True, choices=[('BD', 'Bangladesh'), ('CHN', 'China')], max_length=50, null=True)),
                ('color', models.CharField(blank=True, max_length=250, null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products_fabrictextileproducts_related', related_query_name='products_fabrictextileproductss', to='products.brand')),
                ('fabrictextile_product_type', models.ManyToManyField(related_name='fabrictextile_product_types', related_query_name='fabrictextile_product_type', to='products.Category')),
                ('supplier', models.ManyToManyField(blank=True, related_name='products_fabrictextileproducts_related', related_query_name='products_fabrictextileproductss', to='products.Supplier')),
            ],
            options={
                'verbose_name': 'Fabric and Textile Products',
                'verbose_name_plural': 'Fabric and Textile Products',
            },
        ),
    ]
