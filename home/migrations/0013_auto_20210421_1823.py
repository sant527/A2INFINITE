# Generated by Django 3.1.7 on 2021-04-21 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20210421_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='pkg_feature_1',
            new_name='pkg_feature',
        ),
        migrations.RemoveField(
            model_name='package',
            name='pkg_feature_2',
        ),
        migrations.RemoveField(
            model_name='package',
            name='pkg_feature_3',
        ),
        migrations.RemoveField(
            model_name='package',
            name='pkg_feature_4',
        ),
        migrations.RemoveField(
            model_name='package',
            name='pkg_feature_5',
        ),
        migrations.RemoveField(
            model_name='package',
            name='pkg_feature_6',
        ),
    ]
