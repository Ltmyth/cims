# Generated by Django 4.0.6 on 2022-09-22 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=80)),
                ('doctor', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=80)),
                ('test_name', models.CharField(max_length=200)),
                ('diagnosis', models.CharField(max_length=200)),
                ('time_of_visit', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_name', models.CharField(max_length=80)),
                ('stock', models.CharField(max_length=200)),
                ('prescribed_to', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80)),
                ('symptoms', models.CharField(max_length=200)),
                ('diagnosis', models.CharField(max_length=200)),
                ('time_of_visit', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
