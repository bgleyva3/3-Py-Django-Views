# Generated by Django 2.2.24 on 2021-11-03 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_remove_lesson_students'),
        ('students', '0002_auto_20211101_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='lessons',
            field=models.ManyToManyField(related_name='students', to='lessons.Lesson'),
        ),
    ]