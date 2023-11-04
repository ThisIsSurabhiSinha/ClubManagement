# Generated by Django 4.2.5 on 2023-11-03 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_event'),
        ('trendles', '0004_subclub_leader1mail_subclub_leader1phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChitrachayaImages',
            fields=[
                ('media_type', models.CharField(choices=[('image', 'Image'), ('video', 'Video')], max_length=10)),
                ('media_file', models.FileField(blank=True, default='media/trendles/images/unknown.png', help_text='Upload an image file.', null=True, upload_to='trendles/images/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('subclub_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('majorclub_name', models.CharField(blank=True, max_length=100, null=True)),
                ('uploaded_on', models.DateField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.event')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.student')),
            ],
        ),
    ]