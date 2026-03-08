# Diagnostic Lab API System

A simple backend system for managing diagnostic lab patients and reports.

## Features

- Register Patient
- Upload Lab Report (PDF)
- Fetch Patient Reports
- Simulated SMS notification

## Tech Stack

- Python
- Django
- Django REST Framework

## Setup

Clone repository

git clone https://github.com/yourusername/diagnostic-lab-api.git

Create virtual environment

python -m venv venv

Install dependencies

pip install -r requirements.txt

Run migrations

python manage.py migrate

Run server

python manage.py runserver

## API Endpoints

POST /patients

POST /reports

GET /patients/{id}/reports
