# Generated by Django 4.0.4 on 2023-07-24 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0010_rename_end_date_setting_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='enable',
            new_name='enabled',
        ),
    ]