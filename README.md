# django-traffic-manager

A Django web application for reporting and managing traffic incidents and analyzing accident hotspots.

## Features

This project provides a system for both public reporting and internal management of traffic incidents.

* **Public Incident Reporting:** A simple form allows anyone to report the location, type, and details of a traffic incident.
* **Operator Dashboard:** A secure, login-required dashboard for traffic operators.
    * Displays a **live map** (using Leaflet.js) showing locations of active incidents.
    * Lists active incidents, available response units, currently dispatched units ("Active Duty"), and high-congestion areas.
    * Includes a **"Quick-Add Congestion"** form for fast reporting.
* **Incident Management:** Operators can view details for each incident.
    * Assign available response units (Police, Ambulance, etc.) to an incident.
    * Add time-stamped **log entries/comments** to track progress.
    * Mark incidents as "Closed" once resolved.
* **Hotspot Analysis:** An analysis page that queries the database to show which locations have the highest number of reported incidents, helping to identify problematic areas.
* **User Authentication:** Uses Django's built-in authentication system for operator logins.

## Technology Stack

* **Backend:** Python 3, Django Web Framework
* **Database:** SQLite (default for development)
* **Frontend:** HTML, Tailwind CSS (via CDN)
* **Mapping:** Leaflet.js (via CDN)

## Setup and Installation

Follow these steps to set up the project locally:

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd django-traffic-manager
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # On Windows
    python -m venv venv
    .\venv\Scripts\Activate.ps1

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install django
    # (If you add more packages later, create a requirements.txt and use: pip install -r requirements.txt)
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a superuser (for accessing the admin panel and operator dashboard):**
    ```bash
    python manage.py createsuperuser
    ```
    (Follow the prompts to set a username, email, and password)

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7.  Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1.  **Public Reporting:**
    * Navigate to `http://127.0.0.1:8000/report/`.
    * Fill out the form and submit.

2.  **Operator Access:**
    * Navigate to `http://127.0.0.1:8000/accounts/login/` (or the main page if not logged in).
    * Log in using the superuser credentials you created.
    * You will be redirected to the main Operator Dashboard (`/`).

3.  **Managing Incidents:**
    * From the dashboard, click on an incident in the "Active Incidents" list or on a map pin popup.
    * On the Incident Detail page:
        * Use the "Assign Unit" form to dispatch an available unit.
        * Use the "Add New Log Entry" form to add updates.
        * Click "Close Incident" when resolved.

4.  **Viewing Hotspots:**
    * Click the "Hotspots" link in the navigation bar (or go to `/hotspots/`).
    * View the sorted list of locations with the most incidents.

5.  **Admin Panel (Optional):**
    * Navigate to `http://127.0.0.1:8000/admin/`.
    * Log in with superuser credentials.
    * From here, you can manually manage Incidents, Response Units, Traffic Reports, and Incident Logs. (Crucial for adding initial Response Units!).
  
## Project Screenshots

![Project Screenshot 1](django-traffic-manager/Django Project/traffic_manager/images/image1.png)
![Project Screenshot 2](django-traffic-manager/Django Project/traffic_manager/images/image2.png)
![Project Screenshot 3](django-traffic-manager/Django Project/traffic_manager/images/image3.png)
![Project Screenshot 4](django-traffic-manager/Django Project/traffic_manager/images/image4.png)
![Project Screenshot 5](django-traffic-manager/Django Project/traffic_manager/images/image5.png)
![Project Screenshot 6](django-traffic-manager/Django Project/traffic_manager/images/image6.png)
![Project Screenshot 7](django-traffic-manager/Django Project/traffic_manager/images/image7.png)
![Project Screenshot 9](django-traffic-manager/Django Project/traffic_manager/images/image9.png)
![Project Screenshot 10](django-traffic-manager/Django Project/traffic_manager/images/image10.png)
![Project Screenshot 11](django-traffic-manager/Django Project/traffic_manager/images/image11.png)
![Project Screenshot 12](django-traffic-manager/Django Project/traffic_manager/images/image12.png)

## License

This project is licensed under the MIT License - see the LICENSE file for details.


