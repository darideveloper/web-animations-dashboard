# Generated by Django 4.0.4 on 2023-08-02 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0012_remove_setting_date_setting_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='planes')),
                ('amount', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Planes donor',
                'verbose_name_plural': 'Planes donors',
            },
        ),
    ]