# Generated by Django 5.1.1 on 2024-09-18 18:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_customer_options_alter_customer_created_at_and_more'),
        ('photo_sessions', '0006_photo_thumbnail'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='session',
            options={'verbose_name': 'Session', 'verbose_name_plural': 'Sessions'},
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='hires'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbs'),
        ),
        migrations.AlterField(
            model_name='session',
            name='acess_token',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Acess token'),
        ),
        migrations.AlterField(
            model_name='session',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='session',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='customers.customer', verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='session',
            name='download_count',
            field=models.IntegerField(default=0, verbose_name='Download count'),
        ),
        migrations.AlterField(
            model_name='session',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='session',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='session',
            name='valid_days',
            field=models.IntegerField(default=15, verbose_name='Valid days'),
        ),
    ]
