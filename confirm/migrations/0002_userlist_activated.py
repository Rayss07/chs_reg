# Generated by Django 2.2.12 on 2022-05-30 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confirm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlist',
            name='activated',
            field=models.TextField(default=0),
        ),
    ]
