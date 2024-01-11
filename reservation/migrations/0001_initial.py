# Generated by Django 4.1.5 on 2023-03-31 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminCheckedTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sallist', models.CharField(max_length=8, null=True, verbose_name='Years')),
                ('mahlist', models.CharField(blank=True, max_length=24, null=True, verbose_name='month')),
                ('roozlist', models.CharField(blank=True, max_length=24, null=True, verbose_name='Day')),
                ('timelist', models.CharField(blank=True, max_length=44, null=True, verbose_name='time')),
            ],
        ),
        migrations.CreateModel(
            name='RezervModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_service', models.BooleanField(default=False)),
                ('Interim_service', models.BooleanField(default=False)),
                ('Add_a_mot', models.BooleanField(default=False)),
                ('Wheelaligment', models.BooleanField(default=False)),
                ('Diagnose', models.BooleanField(default=False)),
                ('Tyres', models.BooleanField(default=False)),
                ('Clutches', models.BooleanField(default=False)),
                ('Suspension', models.BooleanField(default=False)),
                ('Cambelt', models.BooleanField(default=False)),
                ('Exhaust', models.BooleanField(default=False)),
                ('Brakes', models.BooleanField(default=False)),
                ('Batteries', models.BooleanField(default=False)),
                ('other', models.TextField(blank=True, null=True)),
                ('Firstname', models.CharField(max_length=80, verbose_name='Firts name')),
                ('Lastname', models.CharField(max_length=80, verbose_name='last name')),
                ('PhoneNumber', models.CharField(max_length=30, verbose_name='phone number')),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Anything', models.TextField(blank=True, null=True)),
                ('make', models.CharField(blank=True, max_length=10, null=True)),
                ('register', models.CharField(blank=True, max_length=20, null=True)),
                ('delivery', models.BooleanField(default=False)),
                ('fixed', models.BooleanField(default=False)),
                ('sallist', models.CharField(max_length=4, null=True, verbose_name='Years')),
                ('mahlist', models.CharField(max_length=20, null=True, verbose_name='month')),
                ('roozlist', models.CharField(max_length=20, null=True, verbose_name='Day')),
                ('timelist', models.CharField(max_length=40, null=True, verbose_name='time')),
            ],
            options={
                'verbose_name': 'Reserve',
                'verbose_name_plural': 'Reserve',
            },
        ),
    ]