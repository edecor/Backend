# Generated by Django 3.2.10 on 2022-01-04 17:42

from django.db import migrations, models
import django.db.models.deletion
import user_profiles.models.comment
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0007_auto_20211230_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(default='yo'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CommentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', versatileimagefield.fields.VersatileImageField(upload_to=user_profiles.models.comment.return_product_image_directory)),
                ('alt', models.CharField(max_length=50)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profiles.comment')),
            ],
        ),
    ]
