# Generated by Django 3.0 on 2021-11-19 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211119_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='mobile_no',
            field=models.BigIntegerField(null=True),
        ),
    ]
