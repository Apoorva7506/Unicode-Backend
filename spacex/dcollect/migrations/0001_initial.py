# Generated by Django 2.2.4 on 2019-08-19 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.IntegerField()),
                ('rocket_name', models.CharField(max_length=270)),
                ('mission_patch_link', models.URLField(max_length=2000)),
                ('date', models.CharField(max_length=270)),
            ],
        ),
    ]
