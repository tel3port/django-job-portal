# Generated by Django 2.0 on 2020-10-12 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblisting',
            name='listing_kws',
            field=models.TextField(default='job listing', max_length=50000),
        ),
    ]
