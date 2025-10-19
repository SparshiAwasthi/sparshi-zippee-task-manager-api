## Solution-Sparshi-Awasthi

# Task Manager API (Django REST Framework)

## Objective
Built a RESTful API for a task manager application using Django. The API allow users to register, log in, and manage tasks (create, read, update, delete) securely using **JWT authentication**.

## Features
- CRUD operations for tasks  
- JWT authentication (login/register)  
- Pagination (10 tasks per page) and filtering by completion status  
- Role-based permissions (task owner or admin)  
- Swagger and ReDoc documentation  
- Unit tests for API endpoints  

## Tech Stack
- Python 3.10+
- Django 4.x
- Django REST Framework
- Simple JWT for authentication
- Swagger / drf-yasg for API docs
- django-filter for filtering
- Pagination with DRF

## Implementation

1. **Project Setup**
   - Created Django project: `task_manager_application`
   - Created `tasks` app
   - Installed required packages: django, djangorestframework, django-filter, djangorestframework-simplejwt, drf-yasg

2. **Task Model**
   - Created `Task` model with fields:
     - `id` (auto-generated)
     - `title` (string)
     - `description` (text)
     - `completed` (boolean)
     - `created_at` (timestamp)
     - `updated_at` (timestamp)
     - `owner` (user relation)
   - Applied migrations

3. **Serializers & Permissions**
   - `TaskSerializer` for task CRUD operations
   - `UserRegisterSerializer` for user registration
   - `IsOwnerOrAdmin` custom permission for update/delete operations

4. **Views**
   - `TaskViewSet` for all task CRUD endpoints
   - `RegisterView` for user registration
   - JWT authentication implemented

5. **Filtering & Pagination**
   - Pagination: 10 tasks per page
   - Filter by `completed` status
   - Search by `title` or `description`

6. **URLs**
   - `/api/tasks/` → Task CRUD
   - `/api/auth/register/` → User registration
   - `/api/auth/token/` → Obtain JWT token
   - `/swagger/` → API documentation

7. **Testing**
   - Unit tests written in `tasks/tests.py`
   - Tested CRUD operations, authentication, and permissions

## API Endpoints
- POST /api/auth/register/  - User registration
- POST /api/auth/token/     - Obtain JWT token
- GET /api/tasks/           - List all tasks
- POST /api/tasks/          - Create a new task
- GET /api/tasks/{id}/      - Retrieve task details
- PUT /api/tasks/{id}/      - Update task
- DELETE /api/tasks/{id}/   - Delete task

## Setup Instructions
- Clone the repository
- Create a virtual environment
- Install dependencies
- Apply migrations
- Create superuser
- Run the development server
- Access the API
- Run tests

