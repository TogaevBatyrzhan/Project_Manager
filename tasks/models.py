from django.db import models
from django.contrib.auth import get_user_model
from projects.models import Project

User = get_user_model()

class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('on_verification', 'On Verification'),
        ('completed', 'Completed'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    creator = models.ForeignKey(User, related_name='created_tasks', on_delete=models.CASCADE)
    team_lead = models.ForeignKey(User, related_name='task_team_lead', on_delete=models.SET_NULL, null=True, blank=True)
    developer = models.ForeignKey(User, related_name='task_developer', on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='new')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.team_lead = self.project.team_lead
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    def can_change_status(self, user):
        if user == self.creator:
            return True
        return False
