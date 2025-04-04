Database Management – Setup Guide

# Technologies Used
Backend: Django (with Django REST Framework)

Database: SQLite (default)

API Testing: Postman

# Database Schema
Field	Type	Description
id	Integer	Auto-generated primary key
name	String	Name of the app
version	String	App version (e.g., Android version)
description	Text	App/system description (device, memory info)

Create Virtual Environment and Install Dependencies

python -m venv venv
venv\Scripts\activate  

Run Migrations to Setup the Database

python manage.py makemigrations
python manage.py migrate

# Run the Server

python manage.py runserver

API will be live at: http://127.0.0.1:8000/

# Testing API Using Postman
POST /api/add-app/

Description: Add app details to the database.

Method: POST

URL: http://127.0.0.1:8000/api/add-app/

Body (JSON):

{
  "name": "Android System Info",
  "version": "11",
  "description": "Device Model: sdk_gphone_x86_64, Total Memory: 2028176 kB, Available Memory: 1181252 kB"
}

GET /api/get-app/{id}/
Description: Retrieve app details by ID.

Method: GET

Example: http://127.0.0.1:8000/api/get-app/1/

DELETE /api/delete-app/{id}/
Description: Delete app entry by ID.

Method: DELETE

Example: http://127.0.0.1:8000/api/delete-app/1/


# Sample Output (POST Success)

{
  "id": 1,
  "name": "Android System Info",
  "version": "11",
  "description": "Device Model: sdk_gphone_x86_64, Total Memory: 2028176 kB, Available Memory: 1181252 kB"
}