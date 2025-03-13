from django.db import models

# Create your models here.
# see shema docs for details.
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

class Project(models.Model):
    class Status(models.TextChoices):
        OPEN = 'O', 'Open'
        CLOSED = 'C', 'Closed'
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    skills = models.JSONField()
    contributor_expectations = models.TextField()
    discord = models.CharField(max_length=255)
    github = models.CharField(max_length=255)
    post_acceptance_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User)
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.OPEN)

class Application(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'A', 'Active'
        REJECTED = 'R', 'Rejected'
        WITHDRAWN = 'W', 'Withdrawn'
        ACCEPTED = 'Y', 'Accepted'

    status = models.CharField(max_length=1, choices=Status.choices, default=Status.ACTIVE)
    applied_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
