from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project_manager = models.ForeignKey(User, related_name='project_manager', on_delete=models.CASCADE)
    team_lead = models.ForeignKey(User, related_name='team_lead', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if the object is being created (not updating)
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title