# Generated by Django 3.1.3 on 2020-11-23 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0002_auto_20201123_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='stationCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
            ],
        ),
    ]
