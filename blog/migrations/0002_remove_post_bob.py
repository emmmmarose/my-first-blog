# Generated by Django 2.2.9 on 2020-02-01 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='bob',
        ),
    ]
