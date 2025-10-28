from django.urls import path
from . import views

urlpatterns = [
    # Feature 3 & 5: The Dashboard (Homepage for operators)
    path('', views.dashboard_view, name='dashboard'),
    
    # Feature 1: Public Report Form
    path('report/', views.report_incident_view, name='report_incident'),
    
    # Feature 2: Incident Detail/Assign Page
    path('incident/<int:pk>/', views.incident_detail_view, name='incident_detail'),
    
    # Feature 6: Hotspot Analysis Page
    path('hotspots/', views.hotspot_view, name='hotspots'),
]