# Generated by Django 4.1.4 on 2022-12-15 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Drame_ex', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tâche',
            old_name='user',
            new_name='userpk',
        ),
    ]
