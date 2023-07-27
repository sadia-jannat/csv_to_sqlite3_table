# Generated by Django 4.2.3 on 2023-07-25 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('author', models.CharField(max_length=200, verbose_name='author')),
                ('genre', models.CharField(max_length=200, verbose_name='genre')),
                ('height', models.PositiveBigIntegerField(verbose_name='height')),
                ('publisher', models.CharField(max_length=100, verbose_name='publisher')),
            ],
        ),
    ]
