# Generated by Django 4.0.4 on 2022-05-25 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_url', models.FileField(null=True, upload_to='media')),
                ('types', models.CharField(max_length=20)),
                ('sub_type', models.CharField(max_length=30)),
                ('length', models.FloatField()),
                ('business', models.ManyToManyField(to='api.business')),
                ('inflection_time', models.ManyToManyField(to='api.inflectiontime')),
            ],
        ),
    ]
