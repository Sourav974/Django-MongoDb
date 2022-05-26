# Generated by Django 4.0.4 on 2022-05-26 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessComponent1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InflectionTimeComponent1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_field', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LogoSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_x', models.CharField(max_length=10)),
                ('position_y', models.CharField(max_length=10)),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('start_time', models.FloatField()),
                ('end_time', models.FloatField()),
                ('opacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TextBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_x', models.CharField(max_length=10)),
                ('position_y', models.CharField(max_length=10)),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('start_time', models.FloatField()),
                ('end_time', models.FloatField()),
                ('opacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Component1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_url', models.FileField(null=True, upload_to='media')),
                ('types', models.CharField(max_length=20)),
                ('sub_type', models.CharField(max_length=30)),
                ('length', models.FloatField()),
                ('business', models.ManyToManyField(to='component.businesscomponent1')),
                ('inflection_time', models.ManyToManyField(to='component.inflectiontimecomponent1')),
                ('logo_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='component.logoslot')),
                ('text_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='component.textbox')),
            ],
        ),
    ]
