# Generated by Django 4.2.5 on 2023-11-05 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trendles', '0008_marketingoutreachclubfile_financeclubfile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chitrachayaimages',
            name='media_file',
            field=models.FileField(blank=True, default='/media/trendles/images/unknown.png', help_text='Upload an image file.', null=True, upload_to='media/trendles/images/'),
        ),
    ]