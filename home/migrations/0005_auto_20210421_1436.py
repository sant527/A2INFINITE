# Generated by Django 3.1.7 on 2021-04-21 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210417_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classdetails',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='remark',
        ),
    ]
