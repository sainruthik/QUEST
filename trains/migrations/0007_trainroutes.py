# Generated by Django 3.1.3 on 2020-11-24 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0006_delete_trainroutes'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainRoutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=10)),
                ('source1', models.CharField(max_length=10)),
                ('source2', models.CharField(max_length=10)),
                ('source3', models.CharField(max_length=10)),
                ('source4', models.CharField(max_length=10)),
                ('source5', models.CharField(max_length=10)),
                ('source6', models.CharField(max_length=10)),
                ('source7', models.CharField(max_length=10)),
                ('source8', models.CharField(max_length=10)),
                ('source9', models.CharField(max_length=10)),
                ('source10', models.CharField(max_length=10)),
                ('source11', models.CharField(max_length=10)),
                ('source12', models.CharField(max_length=10)),
                ('time1', models.CharField(max_length=20)),
                ('time2', models.CharField(max_length=20)),
                ('time3', models.CharField(max_length=20)),
                ('time4', models.CharField(max_length=20)),
                ('time5', models.CharField(max_length=20)),
                ('time6', models.CharField(max_length=20)),
                ('time7', models.CharField(max_length=20)),
                ('time8', models.CharField(max_length=20)),
                ('time9', models.CharField(max_length=20)),
                ('time10', models.CharField(max_length=20)),
                ('time11', models.CharField(max_length=20)),
                ('time12', models.CharField(max_length=20)),
            ],
        ),
    ]