# Generated by Django 3.0.5 on 2020-06-17 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_profile_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_category',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
