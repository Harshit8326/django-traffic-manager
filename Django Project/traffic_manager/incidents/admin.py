from django.contrib import admin
from .models import Incident, ResponseUnit, TrafficReport, IncidentLog

# Register all 3 models to the admin site
admin.site.register(Incident)
admin.site.register(ResponseUnit)
admin.site.register(TrafficReport)
admin.site.register(IncidentLog)