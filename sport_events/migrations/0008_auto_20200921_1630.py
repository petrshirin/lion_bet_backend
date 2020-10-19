# Generated by Django 3.1.1 on 2020-09-21 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_events', '0007_auto_20200921_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='uniq',
        ),
        migrations.AddField(
            model_name='match',
            name='period_name',
            field=models.CharField(default='1 Тайм', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='score_full',
            field=models.CharField(default='2:1', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='score_period',
            field=models.CharField(default='2:1', max_length=10),
            preserve_default=False,
        ),
    ]
