# Generated by Django 5.1.1 on 2024-10-15 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0004_photoexample'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photoexample',
            old_name='Package',
            new_name='package',
        ),
    ]