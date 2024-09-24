# Generated by Django 5.1.1 on 2024-09-18 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_customer_email_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Customer', 'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
    ]
