# Generated by Django 5.0.6 on 2024-09-17 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_estoque_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='item',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='estoque',
            name='nome',
            field=models.CharField(max_length=255),
        ),
    ]
