# Generated by Django 5.0.1 on 2024-03-05 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NIRFRankPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tlr', models.FloatField()),
                ('rpc', models.FloatField()),
                ('go', models.FloatField()),
                ('oi', models.FloatField()),
                ('perception', models.FloatField()),
                ('predicted_rank', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
