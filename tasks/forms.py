from django import forms
from .models import Task

# Custom Task Form
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'completed']  # Adjust fields based on your Task model