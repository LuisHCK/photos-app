# Generated by Django 5.1.1 on 2024-10-16 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0005_rename_package_photoexample_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='package_thumbnails', verbose_name='Image'),
        ),
    ]
