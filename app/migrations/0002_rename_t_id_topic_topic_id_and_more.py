# Generated by Django 4.1.7 on 2023-04-03 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='t_id',
            new_name='topic_id',
        ),
        migrations.RenameField(
            model_name='webpage',
            old_name='t_id',
            new_name='topic_id',
        ),
    ]
