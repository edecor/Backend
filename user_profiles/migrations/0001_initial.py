# Generated by Django 3.2.10 on 2021-12-20 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_rename_producttype_productimage_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WishItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(choices=[('material', 'Material'), ('bathroom', 'Bathroom'), ('decorations', 'Decorations'), ('furniture', 'Furniture'), ('fabric_textile', 'Fabric Tex'), ('hardware_tool', 'Hardware Tool'), ('home_appliances', 'Home Appliances'), ('kitchen', 'Kitchen'), ('landscape_garden', 'Landscape'), ('light', 'Light'), ('rugs_mat', 'Rugs Mat'), ('security_protection', 'Sec Prot')], default='material', max_length=25)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('bathroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.bathroomproducts')),
                ('decorations', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.decorationsproducts')),
                ('fabric_textile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.fabrictextileproducts')),
                ('furniture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.furnitureproducts')),
                ('hardware_tool', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.hardwaretoolproducts')),
                ('home_appliances', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.homeapplianceproducts')),
                ('kitchen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.kitchenproducts')),
                ('landscape_garden', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.landscapeproducts')),
                ('light', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.lightproducts')),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.material')),
                ('rugs_mat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.rugsmatfloorproducts')),
                ('security_protection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.securityprotectionproducts')),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profiles.customer')),
                ('wishes', models.ManyToManyField(to='user_profiles.WishItem')),
            ],
        ),
        migrations.AddConstraint(
            model_name='wishitem',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('bathroom__isnull', True), ('decorations__isnull', True), ('fabric_textile__isnull', True), ('furniture__isnull', True), ('hardware_tool__isnull', True), ('home_appliances__isnull', True), ('kitchen__isnull', True), ('landscape_garden__isnull', True), ('light__isnull', True), ('material__isnull', False), ('rugs_mat__isnull', True), ('security_protection__isnull', True)), models.Q(('bathroom__isnull', False), ('decorations__isnull', True), ('fabric_textile__isnull', True), ('furniture__isnull', True), ('hardware_tool__isnull', True), ('home_appliances__isnull', True), ('kitchen__isnull', True), ('landscape_garden__isnull', True), ('light__isnull', True), ('material__isnull', True), ('rugs_mat__isnull', True), ('security_protection__isnull', True)), models.Q(('bathroom__isnull', True), ('decorations__isnull', False), ('fabric_textile__isnull', True), ('furniture__isnull', True), ('hardware_tool__isnull', True), ('home_appliances__isnull', True), ('kitchen__isnull', True), ('landscape_garden__isnull', True), ('light__isnull', True), ('material__isnull', True), ('rugs_mat__isnull', True), ('security_protection__isnull', True)), models.Q(('bathroom__isnull', True), ('decorations__isnull', True), ('fabric_textile__isnull', True), ('furniture__isnull', False), ('hardware_tool__isnull', True), ('home_appliances__isnull', True), ('kitchen__isnull', True), ('landscape_garden__isnull', True), ('light__isnull', True), ('material__isnull', True), ('rugs_mat__isnull', True), ('security_protection__isnull', True)), models.Q(('bathroom__isnull', True), ('decorations__isnull', True), ('fabric_textile__isnull', False), ('furniture__isnull', True), ('hardware_tool__isnull', True), ('home_appliances__isnull', True), ('kitchen__isnull', True), ('landscape_garden__isnull', True), ('light__isnull', True), ('material__isnull', True), ('rugs_mat__isnull', True), ('security_protection__isnull', True)), models.Q(('bathroom__isnull', True), ('decorations__isnull', True), ('fabric_textile__isnull', True), ('furniture__isnull', True), ('hardware_tool__isnull', False), ('home_appliances__isnull', True), ('kitchen__isnull', True), ('landscape_garden__isnull', True), ('light__isnull', True), ('material__isnull', True), ('rugs_mat__isnull', True), ('security_protection__isnull', True)), models.Q(('bathroom__isnull', True), ('decorations__isnull', True), ('fabric_textile__isnull', True), ('furniture__isnull', True), ('hardware_tool__isnull', True), ('home_appliances__isnull', False), ('kitchen__isnull', True), ('landscape_garden__isnull', True), ('light__isnull', True), ('material__isnull', True), ('rugs_mat__isnull', True), ('security_protection__isnull', True)), models.Q(('bathroom__isnull', True), ('decorations__isnull', True), ('fabric_textile__isnull', True), ('furniture__isnull', True), ('hardware_tool__isnull', True), ('home_appliances__isnull', True), ('kitchen__isnull', False), ('landscape_garden__isnull', True), ('light__isnull', True), ('material__isnull', True), ('rugs_mat__isnull', True), ('security_protection__isnull', True)), models.Q(('bathroom__isnull', True), ('decorations__isnull', True), ('fabric_textile__isnull', True), ('furniture__isnull', True), ('hardware_tool__isnull', True), ('home_appliances__isnull', True), ('kitchen__isnull', True), ('landscape_garden__isnull', False), ('light__isnull', True), ('material__isnull', True), ('rugs_mat__isnull', True), ('security_protection__isnull', True)), models.Q(('bathroom__isnull', True), ('decorations__isnull', True), ('fabric_textile__isnull', True), ('furniture__isnull', True), ('hardware_tool__isnull', True), ('home_appliances__isnull', True), ('kitchen__isnull', True), ('landscape_garden__isnull', True), ('light__isnull', False), ('material__isnull', True), ('rugs_mat__isnull', True), ('security_protection__isnull', True)), models.Q(('bathroom__isnull', True), ('decorations__isnull', True), ('fabric_textile__isnull', True), ('furniture__isnull', True), ('hardware_tool__isnull', True), ('home_appliances__isnull', True), ('kitchen__isnull', True), ('landscape_garden__isnull', True), ('light__isnull', True), ('material__isnull', True), ('rugs_mat__isnull', False), ('security_protection__isnull', True)), models.Q(('bathroom__isnull', True), ('decorations__isnull', True), ('fabric_textile__isnull', True), ('furniture__isnull', True), ('hardware_tool__isnull', True), ('home_appliances__isnull', True), ('kitchen__isnull', True), ('landscape_garden__isnull', True), ('light__isnull', True), ('material__isnull', True), ('rugs_mat__isnull', True), ('security_protection__isnull', False)), _connector='OR'), name='user_profiles_wishitem_value_matches_type'),
        ),
    ]
