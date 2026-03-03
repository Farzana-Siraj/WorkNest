 # Worknest - Employee Management System
 A backend-focused Employee Management System built using Django and REST principles.
This project demonstrates authentication, dynamic form creation, employee CRUD operations, and API development using JWT-based authentication.

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
| Layer          | Technology                    |
| -------------- | ----------------------------- |
| Backend        | Python 3.x                    |
| Framework      | Django                        |
| API Layer      | Django REST Framework         |
| Authentication | JWT (Access & Refresh Tokens) |
| Database       | PostgreSQL (Configurable)     |
| Code Quality   | Black, isort, flake8          |
| API Testing    | Postman                       |


## Project Structure
```bash
worknest/
│
├── backend/
│   ├── manage.py
│   ├── worknest/
│   ├── apps/
│   │    ├── accounts/
│   │    ├── employees/
│   │    ├── forms_builder/
│   │    └── common/
│   ├── requirements.txt
└── └──.env
│
├── frontend/
│   ├── pages/
│   |   ├── dashboard.html
│   └── └── index.html
│
├── postman_collection/
│   └── worknest.postman_collection.json
│
├── .gitignore
└── README.md
└── └──.env

```
## Features
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
cd WorkNest/backend
```

### Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```
### Configure Environment Variables
```bash
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://user:password@localhost:5432/db_name
ALLOWED_HOSTS=127.0.0.1,localhost,0.0.0.0
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

## API Testing

- Postman collection included
- All endpoints secured using JWT
- Include access token in Authorization header:
```bash
Bearer <access_token>
```

## Code Quality

Pre-configured with:
- black
- isort
- flake8
- pre-commit hooks
Ensures:
- PEP8 compliance
- Consistent formatting
- Clean imports
- Maintainable code

## Future Enhancements
- Role-based access control (Admin/User)
- Pagination improvements
- Audit logging
- Form templates
- UI with drag-and-drop builder
- Dockerized deployment
- CI/CD integration
- Unit & integration test coverage expansion