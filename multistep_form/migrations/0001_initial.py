# Generated by Django 4.1.3 on 2022-12-01 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MultiStepForm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=255)),
                ('uname', models.CharField(max_length=255)),
                ('pwd', models.CharField(max_length=255)),
                ('cpwd', models.CharField(max_length=255)),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('phno', models.CharField(max_length=255)),
                ('phno_2', models.CharField(max_length=255)),
                ('photo', models.FileField(upload_to='')),
                ('sign', models.FileField(upload_to='')),
            ],
        ),
    ]
