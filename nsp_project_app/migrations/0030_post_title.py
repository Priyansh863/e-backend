# Generated by Django 2.2.5 on 2020-10-16 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsp_project_app', '0029_followers_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Title',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
