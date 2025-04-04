# Android App Info API – Setup Guide

This project is a simple Django REST API that allows you to:

Add app details

Get app details by ID

Delete app details by ID

#  Requirements
Python 3.x

pip (Python package installer)

Virtualenv (recommended)

#  Setup Instructions

1. Create & Activate Virtual Environment (Optional but recommended)

python -m venv venv
venv\Scripts\activate     # On Windows
# source venv/bin/activate   # On Linux/Mac

2. Install Required Packages

pip install django djangorestframework

3.  Run Migrations

python manage.py migrate

4.  Start the Development Server

python manage.py runserver


The server will run at:

http://127.0.0.1:8000/

#  API Endpoints
Method	Endpoint	Description
POST	/api/add-app/	Add a new app to the database
GET	/api/get-app/{id}/	Retrieve app details by ID
DELETE	/api/delete-app/{id}/	Delete app by ID

#  Testing with Postman

Open Postman or any API testing tool.

Use the above endpoints with corresponding methods.

For POST, use raw JSON body like:

json

{
  "name": "Android System Info",
  "version": "11",
  "description": "Device Model: sdk_gphone_x86_64, Total Memory: ..., Available Memory: ..."
}


