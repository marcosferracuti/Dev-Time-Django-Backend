# Generated by Django 4.0.4 on 2022-04-13 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_timelog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='rate',
            field=models.FloatField(default=0),
        ),
    ]
