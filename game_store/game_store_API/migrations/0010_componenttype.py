# Generated by Django 4.0.6 on 2022-07-21 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_store_API', '0009_manufacturer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComponentType',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False)),
            ],
        ),
    ]