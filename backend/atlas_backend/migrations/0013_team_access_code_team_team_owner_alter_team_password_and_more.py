# Generated by Django 5.1.4 on 2025-03-20 11:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atlas_backend', '0012_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='access_code',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='team',
            name='team_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owned_teams', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$870000$EYRqnjkaQG18H3cvDvrPeR$9KMJz8kcwTgI6VgiMDta4l9z6syb5mSuNYUpUvUPPGU=', max_length=128),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
