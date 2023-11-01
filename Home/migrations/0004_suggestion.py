# Generated by Django 4.2.5 on 2023-10-28 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('Home', '0003_alter_student_date_of_birth_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('suggestion_text', models.TextField()),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.student')),
            ],
        ),
    ]
