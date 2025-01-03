# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.core.validators import MinValueValidator, MaxValueValidator
# from django.contrib.auth.models import Groupfrom django.contrib.auth.models import Group

from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    permissions = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    team_size = models.IntegerField(default=1)
    challenge = models.ForeignKey('Challenge', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='atlas_users',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='atlas_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.email

class Challenge(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web'),
        ('crypto', 'Cryptography'),
        ('pwn', 'Binary Exploitation'),
        ('reverse', 'Reverse Engineering'),
        ('forensics', 'Forensics'),
        ('misc', 'Miscellaneous'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    docker_image = models.CharField(max_length=200)
    flag = models.CharField(max_length=200)
    max_points = models.IntegerField(validators=[MinValueValidator(0)])
    max_team_size = models.IntegerField(default=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    flag_answer = models.CharField(max_length=200,default='')

    def __str__(self):
        return self.title

class Container(models.Model):
    STATUS_CHOICES = [
        ('running', 'Running'),
        ('exited', 'Exit'),
        ('error', 'Error'),
    ]

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    container_id = models.CharField(max_length=100)
    ssh_host = models.CharField(max_length=200)
    ssh_port = models.IntegerField()
    ssh_user = models.CharField(max_length=100)
    ssh_key = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='stopped')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.team.name} - {self.challenge.title}"

class Submission(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    points_awarded = models.IntegerField(validators=[MinValueValidator(0)])
    timestamp = models.DateTimeField(auto_now_add=True)
    flag_submitted = models.CharField(max_length=200,default='')

    def __str__(self):
        return f"{self.team.name} - {self.challenge.title}"

    class Meta:
        ordering = ['-timestamp']
