# Generated by Django 3.1.7 on 2021-04-21 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210421_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='feature_10',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='feature'),
        ),
        migrations.AddField(
            model_name='package',
            name='feature_11',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='feature'),
        ),
        migrations.AddField(
            model_name='package',
            name='feature_12',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='feature'),
        ),
        migrations.AddField(
            model_name='package',
            name='feature_6',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='feature'),
        ),
        migrations.AddField(
            model_name='package',
            name='feature_7',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='feature'),
        ),
        migrations.AddField(
            model_name='package',
            name='feature_8',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='feature'),
        ),
        migrations.AddField(
            model_name='package',
            name='feature_9',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='feature'),
        ),
        migrations.AlterField(
            model_name='package',
            name='feature_1',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='feature'),
        ),
        migrations.AlterField(
            model_name='package',
            name='feature_2',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='feature'),
        ),
        migrations.AlterField(
            model_name='package',
            name='feature_3',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='feature'),
        ),
        migrations.AlterField(
            model_name='package',
            name='feature_4',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='feature'),
        ),
        migrations.AlterField(
            model_name='package',
            name='feature_5',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='feature'),
        ),
    ]
