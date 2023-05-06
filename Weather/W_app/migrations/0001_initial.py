# Generated by Django 4.1.7 on 2023-05-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('roll', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('mob', models.CharField(max_length=15)),
                ('pwd', models.CharField(max_length=25)),
            ],
        ),
    ]
