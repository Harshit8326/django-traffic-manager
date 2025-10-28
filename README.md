django-traffic-manager
A Django web application for reporting and managing traffic incidents and analyzing accident hotspots.
Features
This project provides a system for both public reporting and internal management of traffic incidents.
Public Incident Reporting: A simple form allows anyone to report the location, type, and details of a traffic incident.
[Image Placeholder: Screenshot of the public incident report form]
Operator Dashboard: A secure, login-required dashboard for traffic operators.
Displays a live map (using Leaflet.js) showing locations of active incidents.
Lists active incidents, available response units, currently dispatched units ("Active Duty"), and high-congestion areas.
Includes a "Quick-Add Congestion" form for fast reporting.
[Image Placeholder: Screenshot of the main operator dashboard, showing the map and lists]
Incident Management: Operators can view details for each incident.
Assign available response units (Police, Ambulance, etc.) to an incident.
Add time-stamped log entries/comments to track progress.
Mark incidents as "Closed" once resolved.
[Image Placeholder: Screenshot of the incident detail page, showing details, assigned unit, log form, and log history]
Hotspot Analysis: An analysis page that queries the database to show which locations have the highest number of reported incidents, helping to identify problematic areas.
[Image Placeholder: Screenshot of the hotspot analysis page, showing the sorted list of locations]
User Authentication: Uses Django's built-in authentication system for operator logins.
Technology Stack
Backend: Python 3, Django Web Framework
Database: SQLite (default for development)
Frontend: HTML, Tailwind CSS (via CDN)
Mapping: Leaflet.js (via CDN)
Setup and Installation
Follow these steps to set up the project locally:
Clone the repository:
git clone <your-repository-url>
cd django-traffic-manager


Create and activate a virtual environment:
# On Windows
python -m venv venv
.\venv\Scripts\Activate.ps1

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate


Install dependencies:
pip install django
# (If you add more packages later, create a requirements.txt and use: pip install -r requirements.txt)


Apply database migrations:
python manage.py makemigrations
python manage.py migrate


Create a superuser (for accessing the admin panel and operator dashboard):
python manage.py createsuperuser

(Follow the prompts to set a username, email, and password)
Run the development server:
python manage.py runserver


Open your web browser and navigate to http://127.0.0.1:8000/.
Usage
Public Reporting:
Navigate to http://127.0.0.1:8000/report/.
Fill out the form and submit.
[Image Placeholder: GIF or screenshot showing the public reporting process]
Operator Access:
Navigate to http://127.0.0.1:8000/accounts/login/ (or the main page if not logged in).
Log in using the superuser credentials you created.
You will be redirected to the main Operator Dashboard (/).
[Image Placeholder: Screenshot of the operator login page]
Managing Incidents:
From the dashboard, click on an incident in the "Active Incidents" list or on a map pin popup.
On the Incident Detail page:
Use the "Assign Unit" form to dispatch an available unit.
Use the "Add New Log Entry" form to add updates.
Click "Close Incident" when resolved.
[Image Placeholder: GIF or screenshot showing an operator assigning a unit and adding a log entry]
Viewing Hotspots:
Click the "Hotspots" link in the navigation bar (or go to /hotspots/).
View the sorted list of locations with the most incidents.
Admin Panel (Optional):
Navigate to http://127.0.0.1:8000/admin/.
Log in with superuser credentials.
From here, you can manually manage Incidents, Response Units, Traffic Reports, and Incident Logs. (Crucial for adding initial Response Units!).
[Image Placeholder: Screenshot of the Django admin panel showing the Incidents section]
License
This project is licensed under the MIT License - see the LICENSE file for details.
