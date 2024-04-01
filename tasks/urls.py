from django.urls import path
from . import views

# Set Route URL Patterns
urlpatterns = [
    # Root Path - View Tickts
    path('', views.task_view, name='task_view'),
    # Add Ticket Path
    path('add/', views.add_task, name='add_task'),
    # Toggle Path
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
]