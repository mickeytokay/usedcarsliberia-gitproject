# Generated by Django 4.2 on 2023-04-30 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]