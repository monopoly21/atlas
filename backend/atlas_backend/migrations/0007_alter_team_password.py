# Generated by Django 5.1.4 on 2025-02-25 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atlas_backend', '0006_alter_team_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$870000$A4P29GqkBwH5DYh5DaJCSw$WlXe1aGxu797D/KPTlRSZpR1KsT38V+Rd3Fs6sempO0=', max_length=128),
        ),
    ]
