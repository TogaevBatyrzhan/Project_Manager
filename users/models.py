from django.db import models
from django.contrib.auth.models import AbstractUser
from subscription.models import Subscription


class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class User(AbstractUser):
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)