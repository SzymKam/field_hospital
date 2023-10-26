# FIELD HOSPITAL

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies](#technologies)
- [Usage](#usage)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Run in Docker](#run-in-docker)
  - [Running the Development Server](#running-the-development-server)
- [Database](#database)
- [Testing](#testing)
- [Author](#author)

## Project Overview

This project is created to manage workflow and patient flow of field hospital.
It is built using Django 4.2.3. It's made for long and short term mass events,
festivals, disasters and other activities where medical support are needed.
User can create events, manage them, add patients and create medial documentation.
All of these operations are available by API.

## Technologies

The most important technologies used in the project:

- Python 3.11
- Django 4.2.3
- PostgreSQL 16
- Docker 24.0.5,
- DjangoRestFramework 3.14.0
- Nginx 1.25.3
- Pandas 2.0.3
- Plotly 5.16.1
- Pre-commit 3.3.3
- Crispy-bootstrap4 2022.1
- Weasyprint 60.1
- Factory-boy 3.3.0

## Usage

To enter into service you need to have user account. It's for safety reasons - personal information about patients,
treatment, given drugs or diagnose is restricted for medical staff.

#### Main page

![Main page](readme_images/main_page.jpg)
Main page - list of events with status "preparing" or "in progress"

#### Patient page

![patient list_1](readme_images/patient_list_1.jpg)
![patient list_2](readme_images/patient_list_2.jpg)
List of patient from event. There are two tables: of active and discharged patients.
From this side, user can close and update event, add new patient and get list of patient by email or pdf.

![patient list_3](readme_images/patient_list_3.jpg)
Example of pdf file about event with patient list.

![sending_mail](readme_images/sending_mail.jpg)
Choose register user as email receiver. The same information as in PDF will be sent to the e-mail.

![patient_info](readme_images/patient_info.jpg)
Detail of patient. User can check base information, update them, add auth person,
add treatment or download medical documentation.

![treatment_1](readme_images/vital_sign_plot_list.jpg)
Element of treatment: vital signs table and plot. User can choose what kind of signs want to add - it's not necessary to add all at once.

![treatment_2](readme_images/vital_sign_drugs.jpg)
Element of treatment: drugs admitted to patient. Medic can choose drug, unit and dosage form from list.

![medical_doc_pdf](readme_images/medical_doc_pdf.jpg)
Example of medical documentation in pdf.

![create_user](readme_images/create_user.jpg)
Example of form - creating new user. Admin can add user to admin group.

![api_response](readme_images/api_response.jpg)
Example of api response.

## Features

- [Feature 1]: Events - active, completed. User can create, close and review all of them.
- [Feature 2]: Patients - it's possible to add patient into every active event. Patients have own triage colour to help
  making decision of priority.
- [Feature 3]: Every patient has his own treatment, authorized person, and staff person. In treatment can create medical
  documentation, where can add for example: vital signs, drugs, diagnosis.
- [Feature 4]: Staff - list of medical staff.
- [Feature 5]: Users - for administrating service.
- [Feature 6]: PDF download - events list, patient list of every event and medical documentation is available in pdf format.
- [Feature 7]: User can send email with list of patient for each event. For safety reasons it not includes details about treatment.
- [Feature 8]: API - CRUD operations on models are available via API.
- [Feature 8]: Docker - files configured for 3 containers (web app, database and staticfiles server).

## Getting Started

Follow these steps to get your project up and running locally.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SzymKam/field_hospital
   cd src
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Configure your project by setting up environment variables:

- SECRET_KEY - default is randomly generated

Create local server of PostgreSQL, and set variables to connect:

- USER - database user
- PASSWORD - database user password
- HOST - database host
- NAME - database name

For reset user password via email, connect to email service:

- EMAIL_HOST_USER - user of email host
- EMAIL_HOST_PASSWORD - password to email host
- DEFAULT_FROM_EMAIL - email address to send mails

To help set local variables correctly, you can use ".env.dist" file. Copy this file as ".env" and set you variables values.
