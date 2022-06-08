# Generated by Django 4.0.5 on 2022-06-08 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Author Name: ')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Book Title: ')),
                ('page', models.PositiveIntegerField(verbose_name='Number of Pages:')),
                ('author', models.ManyToManyField(related_name='book', to='book.author', verbose_name='Author: ')),
            ],
        ),
    ]
