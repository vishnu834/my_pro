# Generated by Django 5.1 on 2024-08-12 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='PhoneNumber',
        ),
        migrations.RemoveField(
            model_name='information',
            name='date_of_birth',
        ),
    ]
