# Generated by Django 3.0.5 on 2020-04-10 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_students'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
    ]