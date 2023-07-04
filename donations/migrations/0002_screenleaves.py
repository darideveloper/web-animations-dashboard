# Generated by Django 4.0.4 on 2023-06-26 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScreenLeaves',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('donor_frirst_name', models.CharField(max_length=100)),
                ('donor_last_name', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'verbose_name': 'Screen leaves donor',
                'verbose_name_plural': 'Screen leaves donors',
            },
        ),
    ]