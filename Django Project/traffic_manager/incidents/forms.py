from django import forms
from .models import Incident, ResponseUnit, IncidentLog, TrafficReport

# This is a dictionary of Tailwind classes we'll use to style the forms.
# This keeps the styling consistent and out of the HTML.
common_classes = "w-full p-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"

class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['location_name', 'latitude', 'longitude', 'incident_type', 'details']
        widgets = {
            'location_name': forms.TextInput(attrs={'class': common_classes, 'placeholder': 'e.g., "Main St & 2nd Ave"'}),
            'latitude': forms.NumberInput(attrs={'class': common_classes, 'placeholder': 'e.g., 28.6139'}),
            'longitude': forms.NumberInput(attrs={'class': common_classes, 'placeholder': 'e.g., 77.2090'}),
            'incident_type': forms.Select(attrs={'class': common_classes}),
            'details': forms.Textarea(attrs={'class': common_classes, 'placeholder': 'Add any details...', 'rows': 4}),
        }

class AssignUnitForm(forms.ModelForm):
    # This form will ONLY show units that are currently 'Available'
    assigned_unit = forms.ModelChoiceField(
        queryset=ResponseUnit.objects.filter(status='Available'),
        widget=forms.Select(attrs={'class': common_classes})
    )

    class Meta:
        model = Incident
        fields = ['assigned_unit']

# NEW FORM FOR FEATURE 2
class IncidentLogForm(forms.ModelForm):
    class Meta:
        model = IncidentLog
        # We only want the user to fill out the 'text' field
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': common_classes, 
                'placeholder': 'Add a new log entry... (e.g., "Unit 102 on scene")', 
                'rows': 3
            }),
        }

# NEW FORM FOR FEATURE 3
class CongestionReportForm(forms.ModelForm):
    class Meta:
        model = TrafficReport
        # We only want the user to fill out the 'location_name'
        fields = ['location_name']
        widgets = {
            'location_name': forms.TextInput(attrs={
                'class': common_classes, 
                'placeholder': 'Enter location of congestion...'
            }),
        }