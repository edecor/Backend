# Generated by Django 3.2.10 on 2021-12-23 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0005_alter_wishlist_date_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to='user_profiles.customer'),
        ),
    ]
