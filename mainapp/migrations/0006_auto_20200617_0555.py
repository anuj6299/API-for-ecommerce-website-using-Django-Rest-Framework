# Generated by Django 3.0.5 on 2020-06-17 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20200617_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Profile_category',
            field=models.CharField(blank=True, default='User', max_length=100),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
