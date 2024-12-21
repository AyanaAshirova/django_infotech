# Generated by Django 5.1.2 on 2024-11-24 19:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0006_order_phone_alter_order_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainservice',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='Services.servicecategory'),
        ),
    ]
