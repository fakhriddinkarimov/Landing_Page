# Generated by Django 3.2.7 on 2021-10-04 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=100)),
                ('name_ru', models.CharField(max_length=100)),
                ('ordering', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=100)),
                ('name_ru', models.CharField(max_length=100)),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo.region')),
            ],
        ),
    ]