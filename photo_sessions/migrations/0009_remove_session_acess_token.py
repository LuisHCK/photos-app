# Generated by Django 5.1.1 on 2024-09-19 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo_sessions', '0008_alter_photo_options_alter_photo_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='acess_token',
        ),
    ]
