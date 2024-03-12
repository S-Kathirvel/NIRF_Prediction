# Generated by Django 5.0.1 on 2024-03-05 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NIRFPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tlr', models.FloatField()),
                ('rpc', models.FloatField()),
                ('go', models.FloatField()),
                ('oi', models.FloatField()),
                ('perception', models.FloatField()),
                ('year', models.IntegerField()),
                ('predicted_rank', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='NIRFRankPrediction',
        ),
    ]
