# Generated by Django 4.1.2 on 2022-10-24 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
