# Generated by Django 4.2.4 on 2023-08-08 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=100)),
                ('credits', models.IntegerField(default=10)),
                ('game_state', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
