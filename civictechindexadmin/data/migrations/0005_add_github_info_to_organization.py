# Generated by Django 3.0.7 on 2020-11-15 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_notificationsubscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='github_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='github_name',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]
