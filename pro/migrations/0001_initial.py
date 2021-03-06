# Generated by Django 2.2.4 on 2019-11-13 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='station_name')),
                ('lon', models.IntegerField()),
                ('lat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('precipitation', models.FloatField(blank=True, null=True, verbose_name='precipitation')),
                ('temperature', models.FloatField(blank=True, null=True, verbose_name='precipitation')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro.Station')),
            ],
        ),
    ]
