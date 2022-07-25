# Generated by Django 4.0.6 on 2022-07-25 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_store_API', '0003_alter_specifications_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specifications',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specs', to='game_store_API.product'),
        ),
    ]