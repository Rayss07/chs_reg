# Generated by Django 2.2.12 on 2022-06-10 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confirm', '0008_remove_userlist_subtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hotel_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.RenameField(
            model_name='info_basic',
            old_name='birthplace',
            new_name='ethenicity',
        ),
        migrations.RemoveField(
            model_name='info_basic',
            name='birthprovince',
        ),
        migrations.RemoveField(
            model_name='info_basic',
            name='bloodtype',
        ),
        migrations.RemoveField(
            model_name='info_basic',
            name='classroom_grade',
        ),
        migrations.RemoveField(
            model_name='info_basic',
            name='classroom_room',
        ),
        migrations.RemoveField(
            model_name='info_basic',
            name='ethenic',
        ),
        migrations.RemoveField(
            model_name='info_basic',
            name='language_main',
        ),
        migrations.RemoveField(
            model_name='info_basic',
            name='language_other',
        ),
        migrations.RemoveField(
            model_name='info_basic',
            name='latest_school',
        ),
        migrations.RemoveField(
            model_name='info_basic',
            name='latest_school_province',
        ),
        migrations.RemoveField(
            model_name='info_basic',
            name='prefix',
        ),
        migrations.RemoveField(
            model_name='info_basic',
            name='studentid',
        ),
    ]
