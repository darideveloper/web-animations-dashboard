# Generated by Django 4.0.4 on 2023-09-04 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0013_planes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pinata',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('amount', models.IntegerField(default=0, max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Planes',
        ),
    ]
