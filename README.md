 # Worknest - Employee Management System
 A backend-focused Employee Management System built using Django and REST principles.
This project demonstrates authentication, dynamic form creation, employee CRUD operations, and API development using JWT-based authentication.
⚠️ This repository is under active development. Features will be added incrementally.

## Project Overview
This project is developed as part of a Machine Test assignment.
The goal is to build a modular Employee Management System that supports:
- User Authentication (JWT based)
- Profile Management
- Dynamic Form Builder
- Employee Creation using dynamic fields
- Employee Listing with search & filters
- REST API conversion of all features

## Tech Stack
**Backend**: Python, Django, Django REST Framework
**Authentication**: JWT (Access & Refresh Tokens)
**Database**: SQLite (default, configurable)
**Frontend** (Planned): HTML/CSS/JavaScript or JS Framework
**API Testing**: Postman

## Current Status
✅ **Completed**
- Initial Django project setup
- Modular app structure
- Environment configuration
- Code linting setup (Black, isort, flake8)
- Git branching strategy

## In Progress
- JWT Authentication
- Employee CRUD APIs
- Dynamic Form Builder
- API Documentation
- Postman Collection

## Project Structure (Initial)
```bash
worknest/
│
├── backend/
│   ├── manage.py
│   ├── config/
│   ├── apps/
│   │    ├── accounts/
│   │    ├── employees/
│   │    ├── forms_builder/
│   │    └── common/
│   ├── requirements.txt
└── └──.env
│
├── frontend/
│   ├── assets/
│   │    ├── css/
│   │    ├── js/
│   ├── pages/
│   └── index.html
│
├── postman_collection/
│   └── worknest.postman_collection.json
│
├── .gitignore
└── README.md

```
## Planned Features
### Authentication & Profile
- Register
- Login (JWT Access + Refresh Token)
- Change Password
- Profile View/Update

### Dynamic Form Builder
- Create forms with dynamic fields:
- - Text
- - Number
- - Date
- - Password
- - etc.
- Add fields dynamically
- Drag-and-drop reordering (frontend planned)

### Employee Management
- Create employee using selected dynamic form
- Update employee details
- Employee listing
- Search & filter by dynamic fields
- Delete employee

### REST API Conversion
- JWT-based Authentication APIs
- Employee CRUD APIs
- Dynamic Form APIs

## Setup Instructions (Initial)
### clone the repository
```bash
git clone https://github.com/Farzana-Siraj/WorkNest.git
cd WorkNest
```

### Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Migrations
```bash
python manage.py migrate
```

### Start Development Server
```bash
python manage.py runserver

Server will start at:
http://127.0.0.1:8000/
```

## Development Approach
- Modular app-based architecture
- Clean code principles
- Linting from the beginning
- Feature-based branches
- Incremental commits with semantic messages
- API-first design mindset