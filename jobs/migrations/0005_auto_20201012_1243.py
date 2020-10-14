# Generated by Django 2.0 on 2020-10-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20201012_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteMetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(max_length=2000)),
                ('tagline_1', models.CharField(max_length=5000)),
                ('tagline_2', models.CharField(max_length=5000)),
                ('review_1', models.CharField(max_length=8000)),
                ('review_2', models.CharField(max_length=8000)),
                ('review_3', models.CharField(max_length=8000)),
                ('review_4', models.CharField(max_length=8000)),
                ('service_1', models.CharField(max_length=8000)),
                ('service_2', models.CharField(max_length=8000)),
                ('service_3', models.CharField(max_length=8000)),
                ('service_4', models.CharField(max_length=8000)),
                ('service_5', models.CharField(max_length=8000)),
                ('service_6', models.CharField(max_length=8000)),
                ('location', models.CharField(max_length=5000)),
                ('alt_kws', models.CharField(max_length=5000)),
                ('about_site', models.CharField(max_length=15000)),
                ('about_team_member_1', models.CharField(max_length=5000)),
                ('about_team_member_2', models.CharField(max_length=5000)),
            ],
        ),
        migrations.RemoveField(
            model_name='joblisting',
            name='vacancy',
        ),
    ]