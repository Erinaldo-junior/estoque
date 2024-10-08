# Generated by Django 5.0.6 on 2024-09-16 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Nota',
        ),
    ]