# Generated by Django 3.1.1 on 2020-09-22 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_events', '0009_auto_20200921_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='opp_1_icon',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
    ]