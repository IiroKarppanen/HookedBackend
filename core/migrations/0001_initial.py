# Generated by Django 4.0.3 on 2022-08-25 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.CharField(blank=True, max_length=10)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('year', models.CharField(blank=True, max_length=6)),
                ('start_year', models.IntegerField(blank=True)),
                ('end_year', models.IntegerField(blank=True)),
                ('age', models.CharField(blank=True, max_length=15)),
                ('plot', models.CharField(blank=True, max_length=5000)),
                ('revenue', models.IntegerField(blank=True)),
                ('rating', models.FloatField(blank=True)),
                ('runtime', models.CharField(blank=True, max_length=10)),
                ('votes', models.IntegerField(blank=True)),
                ('genres', models.CharField(blank=True, max_length=50)),
                ('kind', models.CharField(blank=True, max_length=10)),
                ('ep_count', models.CharField(blank=True, max_length=5)),
                ('cast', models.CharField(blank=True, max_length=1000)),
                ('image_url', models.CharField(blank=True, max_length=3000)),
            ],
        ),
    ]
