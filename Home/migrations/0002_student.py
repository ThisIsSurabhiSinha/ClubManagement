# Generated by Django 4.2.5 on 2023-10-28 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('program', models.CharField(max_length=50, null=True)),
                ('batch', models.CharField(max_length=4, null=True)),
                ('department', models.CharField(max_length=50, null=True)),
                ('linkedin_profile', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
