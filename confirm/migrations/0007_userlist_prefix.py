# Generated by Django 2.2.12 on 2022-06-06 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confirm', '0006_auto_20220531_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlist',
            name='prefix',
            field=models.TextField(default=None),
        ),
    ]
