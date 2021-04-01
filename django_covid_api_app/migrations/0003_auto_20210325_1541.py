# Generated by Django 3.1.7 on 2021-03-25 10:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_covid_api_app', '0002_auto_20210324_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_user', models.CharField(max_length=30)),
                ('admin_pass', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='fileupload',
            name='file_upload_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_date', models.DateTimeField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_covid_api_app.adminuser')),
                ('file_upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_covid_api_app.fileupload')),
                ('test_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_covid_api_app.testtype')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_covid_api_app.user_tbl')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date_time', models.DateTimeField()),
                ('created_date', models.DateTimeField()),
                ('appointment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_covid_api_app.appointmenttype')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_covid_api_app.adminuser')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_covid_api_app.user_tbl')),
            ],
        ),
    ]