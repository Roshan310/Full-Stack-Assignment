from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=300)
    due_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
