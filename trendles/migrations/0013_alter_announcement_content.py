# Generated by Django 4.2.5 on 2023-11-07 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trendles', '0012_alter_announcement_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
