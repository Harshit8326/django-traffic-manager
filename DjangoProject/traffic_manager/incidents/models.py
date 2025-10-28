from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User # Required for the @login_required decorator

# Choices for our incident types
INCIDENT_TYPES = [
    ('ACCIDENT', 'Accident'),
    ('CONGESTION', 'Heavy Congestion'),
    ('ROAD_WORK', 'Road Work'),
    ('HAZARD', 'Road Hazard'),
]

# Choices for response unit status
STATUS_CHOICES = [
    ('Available', 'Available'),
    ('Dispatched', 'Dispatched'),
    ('On_Scene', 'On Scene'),
    ('Unavailable', 'Unavailable'),
]

class ResponseUnit(models.Model):
    """
    Model for an emergency unit (police, ambulance, etc.)
    """
    name = models.CharField(max_length=100)
    # *** THIS IS THE LINE WE CHANGED ***
    unit_type = models.CharField(max_length=50, choices=[('Police', 'Police'), ('Ambulance', 'Ambulance'), ('Fire', 'Fire'), ('Tow', 'Tow Truck')], default='Police')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')

    def __str__(self):
        return f"{self.name} ({self.get_unit_type_display()})"

class Incident(models.Model):
    """
    Model for a single traffic incident.
    """
    # Feature 1: Incident Logging
    location_name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    incident_type = models.CharField(max_length=50, choices=INCIDENT_TYPES)
    report_time = models.DateTimeField(default=timezone.now)
    
    # Feature 2: Response Management
    assigned_unit = models.ForeignKey(ResponseUnit, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    # *** THIS IS THE NEW FIELD WE ARE ADDING ***
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.location_name
    
    def get_absolute_url(self):
        # This allows us to click on an incident to see its detail page
        return reverse('incident_detail', kwargs={'pk': self.pk})

class TrafficReport(models.Model):
    """
    Model for a general traffic congestion report (not a specific incident)
    """
    # Feature 4: Traffic Monitoring
    location_name = models.CharField(max_length=200)
    congestion_level = models.CharField(max_length=20, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.location_name} - {self.congestion_level}"

# NEW MODEL FOR FEATURE 2
class IncidentLog(models.Model):
    """
    Model for storing a log entry (a comment) related to a specific incident.
    """
    # Link this log to one incident. If the incident is deleted, delete these logs.
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)

    # Link this log to the user who wrote it.
    operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # The text content of the log
    text = models.TextField()

    # Automatically add a timestamp when the log is created
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Show this in the admin panel
        return f"Log for Incident #{self.incident.id} @ {self.timestamp.strftime('%Y-%m-%d %H:%M')}"