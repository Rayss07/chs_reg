# Generated by Django 2.2.12 on 2022-05-30 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confirm', '0003_auto_20220530_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlist',
            name='activated',
            field=models.BooleanField(default=True),
        ),
    ]
