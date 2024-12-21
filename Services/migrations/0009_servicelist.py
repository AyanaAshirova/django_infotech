# Generated by Django 5.1.2 on 2024-12-06 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0008_mainservice_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('services', models.ManyToManyField(to='Services.service')),
            ],
        ),
    ]