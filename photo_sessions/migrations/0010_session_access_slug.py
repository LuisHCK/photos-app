# Generated by Django 5.1.1 on 2024-09-19 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_sessions', '0009_remove_session_acess_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='access_slug',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Acess slug'),
        ),
    ]
