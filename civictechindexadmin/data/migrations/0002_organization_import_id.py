# Generated by Django 3.0.5 on 2020-06-28 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='import_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
