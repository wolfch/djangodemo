# Generated by Django 3.2.5 on 2021-07-13 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_remove_democonfig_db_foo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DemoConfig',
            new_name='Config',
        ),
    ]