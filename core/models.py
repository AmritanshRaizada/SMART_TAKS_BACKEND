from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Task(models.Model):
    STATUS_CHOICES = [('TODO', 'Todo'), ('INPROGRESS', 'In Progress'), ('DONE', 'Done')]
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

class ActivityLog(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    prev_assignee = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='prev_assignee')
    prev_status = models.CharField(max_length=20, choices=Task.STATUS_CHOICES)
    prev_due_date = models.DateField()