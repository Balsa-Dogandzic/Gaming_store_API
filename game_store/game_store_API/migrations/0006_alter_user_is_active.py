# Generated by Django 4.0.6 on 2022-07-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_store_API', '0005_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
