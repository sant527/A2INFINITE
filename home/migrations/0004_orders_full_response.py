# Generated by Django 3.1.7 on 2021-04-24 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='full_response',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
