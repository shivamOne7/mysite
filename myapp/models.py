from django.db import models

# Create your models here.
class Item(models.Model):
    item_name=models.CharField(max_length=255)
    item_price=models.CharField(max_length=255)
    item_decs=models.CharField(max_length=255)

    def __str__(self):
        return self.item_name

class FeatureFlag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# models.py
from django.db import models
from django.contrib.auth.models import User

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    extra_data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.action}"



class ScheduledJob(models.Model):
    name = models.CharField(max_length=255)
    run_at = models.DateTimeField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    


from django.utils import timezone

class EmailTask(models.Model):
    # Job Content
    subject = models.CharField(max_length=255)
    recipient = models.EmailField()
    message = models.TextField()

    # Scheduling (Delayed Job Feature)
    run_at = models.DateTimeField(help_text="When the job should run")
    
    # Retry Logic (Retry System Feature)
    attempts = models.IntegerField(default=0)
    max_retries = models.IntegerField(default=5)
    
    # Status Tracking
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('success', 'Success'), ('failed', 'Failed')],
        default='pending'
    )
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject} to {self.recipient}"