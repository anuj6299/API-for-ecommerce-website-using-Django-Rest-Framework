# Generated by Django 3.0.5 on 2020-06-21 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_item_item_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_packed',
            field=models.BooleanField(default=False),
        ),
    ]
