# Generated by Django 4.2.6 on 2023-10-31 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FootballPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.CharField(help_text='ID', max_length=20)),
                ('p_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('team_name', models.CharField(max_length=100)),
            ],
        ),
    ]
