# Generated by Django 2.2.3 on 2019-07-29 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190723_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos_location',
            name='activate',
            field=models.BooleanField(default=True),
        ),
    ]
