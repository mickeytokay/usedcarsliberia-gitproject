# Generated by Django 4.2 on 2023-05-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_car_county'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='body_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
