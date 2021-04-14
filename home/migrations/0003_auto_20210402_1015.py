# Generated by Django 3.1.7 on 2021-04-02 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_sheet'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.CharField(blank=True, default=None, max_length=60, verbose_name='ClassName')),
                ('classTitle', models.CharField(blank=True, default=None, max_length=200, verbose_name='ClassTitle')),
                ('remark', models.TextField(blank=True, default=None, max_length=600, verbose_name='remark')),
            ],
        ),
        migrations.CreateModel(
            name='Explain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explaintitle', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='explaintitle')),
                ('body', models.TextField(blank=True, default=None, max_length=6000, verbose_name='SubTopicName')),
                ('imgBlack', models.ImageField(blank=True, default=None, null=True, upload_to='uploads/gallery/Black/')),
                ('imgWhite', models.ImageField(blank=True, default=None, null=True, upload_to='uploads/gallery/White/')),
                ('imgColor', models.ImageField(blank=True, default=None, null=True, upload_to='uploads/gallery/Color/')),
                ('remark', models.CharField(blank=True, default=None, max_length=60, verbose_name='remark')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubjectName', models.CharField(blank=True, default=None, max_length=60, verbose_name='SubjectName')),
                ('SubjectTitle', models.CharField(blank=True, default=None, max_length=200, verbose_name='SubjectTitle')),
                ('remark', models.TextField(blank=True, default=None, max_length=600, verbose_name='remark')),
                ('className', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ClassDetails', to='home.classdetails')),
            ],
        ),
        migrations.CreateModel(
            name='SubTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubTopicName', models.CharField(blank=True, default=None, max_length=60, verbose_name='SubTopicName')),
                ('subtopicTitle', models.CharField(blank=True, default=None, max_length=200, verbose_name='subtopicTitle')),
                ('remark', models.TextField(blank=True, default=None, max_length=600, verbose_name='remark')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TopicName', models.CharField(blank=True, default=None, max_length=60, verbose_name='TopicName')),
                ('topicTitle', models.CharField(blank=True, default=None, max_length=200, verbose_name='topicTitle')),
                ('remark', models.TextField(blank=True, default=None, max_length=600, verbose_name='remark')),
                ('Subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Subject', to='home.subject')),
            ],
        ),
        migrations.DeleteModel(
            name='Sheet',
        ),
        migrations.AddField(
            model_name='subtopic',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic', to='home.topic'),
        ),
        migrations.AddField(
            model_name='explain',
            name='SubTopic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SubTopic', to='home.subtopic'),
        ),
    ]