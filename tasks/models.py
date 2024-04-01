from django.db import models

# Task Data Model
class Task(models.Model):
    # Description Field Structure
    description = models.CharField(max_length=255)
    # Completed Status Field Structure
    completed = models.BooleanField(default=False)
    # Created Timeframe Field Structure
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
