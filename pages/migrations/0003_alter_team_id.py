# Generated by Django 4.2 on 2023-04-30 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20230430_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
