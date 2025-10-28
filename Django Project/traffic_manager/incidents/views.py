from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Incident, ResponseUnit, TrafficReport, IncidentLog
from .forms import IncidentReportForm, AssignUnitForm, IncidentLogForm, CongestionReportForm

# Create your views here.
@login_required
def dashboard_view(request):
    """
    FEATURE 3, 4, 5: The main operator dashboard.
    Shows the map, active incidents, available units, and congestion.
    """
    active_incidents = Incident.objects.filter(is_active=True).order_by('-report_time')
    available_units = ResponseUnit.objects.filter(status='Available')
    high_congestion_reports = TrafficReport.objects.filter(congestion_level='High').order_by('-last_updated')
    # Get all units that are NOT 'Available' or 'Unavailable'
    busy_units = ResponseUnit.objects.filter(status__in=['Dispatched', 'On_Scene'])

    # --- NEW LOGIC FOR FEATURE 3 ---
    # Initialize the form for a GET request
    congestion_form = CongestionReportForm()

    # Check if the form was submitted (a POST request)
    if request.method == 'POST' and 'action' in request.POST and request.POST['action'] == 'add_congestion':
        congestion_form = CongestionReportForm(request.POST) # Get the submitted data
        if congestion_form.is_valid():
            new_congestion = congestion_form.save(commit=False)
            new_congestion.congestion_level = 'High' # Automatically set to 'High'
            new_congestion.save()
            # Ensure this return is indented correctly under the 'if is_valid():'
            return redirect('dashboard') # Redirect to clear the form
    # --- END OF NEW LOGIC ---

    # This context dictionary should be at the same indentation level
    # as the start of the 'if request.method == POST...' block above it.
    context = {
        'incidents': active_incidents,
        'units': available_units,
        'reports': high_congestion_reports,
        'busy_units': busy_units,
        'congestion_form': congestion_form, 
    }
    # This final return should be at the same indentation level
    # as the start of the function definition ('def dashboard_view...')
    return render(request, 'incidents/dashboard.html', context)

@login_required
def incident_detail_view(request, pk):
    """
    FEATURE 2: The detail page for a single incident.
    Handles THREE forms: Assigning Unit, Closing Incident, and Adding Log.
    """
    incident = get_object_or_404(Incident, pk=pk)

    # Get all logs for this incident, newest first
    logs = IncidentLog.objects.filter(incident=incident).order_by('-timestamp')

    # Initialize our two forms for the GET request
    form = AssignUnitForm(instance=incident) # The "Assign Unit" form
    log_form = IncidentLogForm()             # The new "Add Log" form

    if request.method == 'POST':

        # --- Check which button was pressed ---

        # 1. Check for "CLOSE INCIDENT" button
        if 'action' in request.POST and request.POST['action'] == 'close_incident':
            incident.is_active = False
            incident.save()

            if incident.assigned_unit:
                unit = incident.assigned_unit
                unit.status = 'Available'
                unit.save()

            return redirect('dashboard')

        # 2. Check for "ADD LOG" button
        elif 'action' in request.POST and request.POST['action'] == 'add_log':
            # Re-bind log_form with the POST data
            log_form = IncidentLogForm(request.POST) 
            if log_form.is_valid():
                new_log = log_form.save(commit=False)
                new_log.incident = incident
                new_log.operator = request.user
                new_log.save()
            # Redirect to the same page (to clear the form)
            return redirect('incident_detail', pk=incident.pk)

        # 3. Check for "ASSIGN UNIT" button 
        # (We will add name="action" value="assign_unit" to this button in the next step)
        elif 'action' in request.POST and request.POST['action'] == 'assign_unit':
            # Re-bind the 'form' with POST data
            form = AssignUnitForm(request.POST, instance=incident) 
            if form.is_valid():
                assigned_incident = form.save()
                if assigned_incident.assigned_unit:
                    unit = assigned_incident.assigned_unit
                    unit.status = 'Dispatched'
                    unit.save()
            # Redirect to the same page
            return redirect('incident_detail', pk=incident.pk)

    # This context is for the GET request
    # It passes all logs and the two empty forms to the template
    context = {
        'incident': incident,
        'form': form,
        'log_form': log_form,  # Pass the log form
        'logs': logs         # Pass the list of old logs
    }
    return render(request, 'incidents/incident_detail.html', context)

@login_required
def hotspot_view(request):
    """
    FEATURE 6: The Hotspot Analysis Page.
    """
    # This query groups incidents by location, counts them, and orders from most to least.
    hotspots = (
        Incident.objects
        .values('location_name', 'latitude', 'longitude')
        .annotate(incident_count=Count('id'))
        .order_by('-incident_count')
    )
    
    context = {
        'hotspots': hotspots
    }
    return render(request, 'incidents/hotspots.html', context)


def report_incident_view(request):
    """
    FEATURE 1: The public-facing incident report form.
    """
    if request.method == 'POST':
        form = IncidentReportForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'incidents/report_success.html')
    else:
        form = IncidentReportForm()
        
    context = {
        'form': form
    }
    return render(request, 'incidents/report_form.html', context)

