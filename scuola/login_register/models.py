from django.db import models
from django.utils import timezone


class Register(models.Model):
    date = models.DateField("Date", default=timezone.now)
    name = models.CharField(max_length=30, null=True, blank=True)
    surname = models.CharField(max_length=30, null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=30, null=True, blank=True)
