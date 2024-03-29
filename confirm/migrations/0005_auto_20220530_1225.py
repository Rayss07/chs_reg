# Generated by Django 2.2.12 on 2022-05-30 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confirm', '0004_auto_20220530_0906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcard', models.CharField(max_length=13)),
                ('home_id', models.TextField()),
                ('village_id', models.TextField()),
                ('village_name', models.TextField()),
                ('parish', models.TextField()),
                ('alley', models.TextField()),
                ('road', models.TextField()),
                ('district', models.TextField()),
                ('city', models.TextField()),
                ('zip_code', models.TextField()),
                ('level_address', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='userlist',
            name='activated',
            field=models.BooleanField(default=False),
        ),
    ]
