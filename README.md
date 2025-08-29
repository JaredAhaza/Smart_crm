# Smart CRM - Software Developer Assessment

A comprehensive Customer Relationship Management (CRM) system built with Django REST Framework backend and Vue.js frontend, featuring role-based authentication, audit trails, and automated reminders.

##  Features

### Core Functionality
- **Leads Management**: Create, read, update, delete leads with status tracking
- **Contacts Management**: Manage contacts linked to leads
- **Notes System**: Add notes to specific leads
- **Reminders**: Schedule and track reminders with Celery automation
- **Correspondence Tracking**: Log emails, calls, and meetings for contacts
- **Audit Trail**: Complete logging of all changes with user attribution

### Authentication & Authorization
- **JWT Authentication**: Secure token-based authentication
- **Role-Based Access Control**: 
  - **Manager**: Full access (create, read, update, delete)
  - **Agent**: Restricted access (cannot delete leads or contacts)

### Advanced Features
- **Search & Filtering**: Real-time search and filtering for leads and contacts
- **Real-time Updates**: Live data updates across the application
- **Responsive Design**: Modern UI built with Tailwind CSS

## 🛠️ Technology Stack

### Backend
- **Django 5.0.6**: Web framework
- **Django REST Framework 3.15.2**: API framework
- **PostgreSQL**: Primary database
- **Redis**: Message broker for Celery
- **Celery**: Background task processing
- **JWT**: Authentication tokens

### Frontend
- **Vue.js 3**: Progressive JavaScript framework
- **Vite**: Build tool and dev server
- **Tailwind CSS**: Utility-first CSS framework
- **Axios**: HTTP client

### Infrastructure
- **Docker**: Containerization
- **Docker Compose**: Multi-container orchestration

## 📋 Prerequisites

- Docker and Docker Compose installed
- Git

##  Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/JaredAhaza/Smart_crm.git
cd Smart_crm
```

### 2. Start the Application
```bash
docker-compose up --build
```

### 3. Setup Initial Data
```bash
# Create superuser
docker-compose exec backend python manage.py createsuperuser

# Create default roles (in Django shell)
docker-compose exec backend python manage.py shell
```
```python
from django.contrib.auth.models import Group
Group.objects.get_or_create(name='manager')
Group.objects.get_or_create(name='agent')
exit()
```

### 4. Access the Application
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **Django Admin**: http://localhost:8000/admin
- **API Browser**: http://localhost:8000/api/

##  API Endpoints

### Authentication
- `POST /api/token/` - Login and get JWT tokens
- `POST /api/token/refresh/` - Refresh access token
- `POST /api/register/` - Register new user with role

### Leads
- `GET /api/leads/` - List leads (supports filtering and search)
- `POST /api/leads/` - Create new lead
- `GET /api/leads/{id}/` - Get specific lead
- `PUT /api/leads/{id}/` - Update lead
- `DELETE /api/leads/{id}/` - Delete lead (manager only)

### Contacts
- `GET /api/contacts/` - List contacts (supports filtering and search)
- `POST /api/contacts/` - Create new contact
- `GET /api/contacts/{id}/` - Get specific contact
- `PUT /api/contacts/{id}/` - Update contact
- `DELETE /api/contacts/{id}/` - Delete contact (manager only)

### Notes
- `GET /api/notes/` - List notes (filtered by lead)
- `POST /api/notes/` - Create new note

### Reminders
- `GET /api/reminders/` - List reminders (filtered by lead)
- `POST /api/reminders/` - Create new reminder
- `PUT /api/reminders/{id}/` - Update reminder
- `DELETE /api/reminders/{id}/` - Delete reminder

### Correspondence
- `GET /api/correspondence/` - List correspondence (filtered by contact)
- `POST /api/correspondence/` - Create new correspondence
- `PUT /api/correspondence/{id}/` - Update correspondence
- `DELETE /api/correspondence/{id}/` - Delete correspondence

### Audit Trail
- `GET /api/audit/` - List audit logs (supports filtering)

##  Search & Filtering

### Leads
- **Search**: By name and status
- **Filters**: Status, owner, creation date
- **Ordering**: By creation date, update date, name

### Contacts
- **Search**: By first name, last name, email, phone
- **Filters**: Lead, owner, creation date
- **Ordering**: By creation date, update date, last name

## 🔐 Role-Based Permissions

### Manager
- Full CRUD access to all resources
- Can delete leads and contacts
- Access to all features

### Agent
- Read, create, and update access
- **Cannot delete** leads or contacts
- Full access to notes, reminders, and correspondence

## 📊 Audit Trail

The system automatically logs all changes to leads and contacts:
- **Created**: When new records are added
- **Updated**: When records are modified (with field-level changes)
- **Deleted**: When records are removed
- **User attribution**: Tracks who made each change
- **Timestamp**: Records when changes occurred

## 🏗️ Architecture Decisions

### Backend Architecture
- **Django REST Framework**: Chosen for rapid API development and excellent documentation
- **PostgreSQL**: Production-ready database with JSON field support for audit logs
- **Celery + Redis**: Asynchronous task processing for reminders
- **JWT Authentication**: Stateless authentication suitable for API-first architecture

### Frontend Architecture
- **Vue.js 3**: Modern reactive framework with excellent developer experience
- **Composition API**: Better TypeScript support and code organization
- **Tailwind CSS**: Rapid UI development with consistent design system
- **Axios**: Reliable HTTP client with request/response interceptors

### Containerization
- **Docker Compose**: Easy local development and deployment
- **Multi-stage builds**: Optimized container sizes
- **Volume mounting**: Hot reload for development

## 🔧 Development Setup

### Local Development (without Docker)
```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend
cd frontend
npm install
npm run dev
```

### Environment Variables
```bash
# Backend
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=1
POSTGRES_DB=smartcrm
POSTGRES_USER=smartcrm
POSTGRES_PASSWORD=smartcrm
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
REDIS_URL=redis://localhost:6379/0

# Frontend
VITE_API_BASE=http://localhost:8000/api
```

## 🧪 Testing

### Manual Testing Checklist
- [ ] User registration and login
- [ ] Role-based permissions (manager vs agent)
- [ ] CRUD operations for leads and contacts
- [ ] Search and filtering functionality
- [ ] Notes and reminders creation
- [ ] Correspondence logging
- [ ] Audit trail verification
- [ ] Celery reminder processing

## 🚀 Deployment

### Production Considerations
- Use environment variables for sensitive data
- Configure proper CORS settings
- Set up SSL/TLS certificates
- Configure database backups
- Set up monitoring and logging
- Use production-grade Redis and PostgreSQL

##  Assumptions Made

1. **User Management**: Users are created by administrators or self-registration
2. **Data Validation**: Basic validation with option to extend
3. **Email Integration**: Reminder system is prepared for email integration
4. **File Uploads**: Not implemented but architecture supports it
5. **Real-time Features**: WebSocket integration not implemented but possible
6. **Mobile Support**: Responsive design but no mobile app

## 🔮 Future Improvements

### Short Term
- [ ] Email integration for reminders
- [ ] File upload for correspondence
- [ ] Advanced reporting and analytics
- [ ] Bulk operations for leads/contacts
- [ ] Email templates for correspondence

### Long Term
- [ ] Real-time notifications
- [ ] Mobile application
- [ ] Advanced workflow automation
- [ ] Integration with external CRM systems
- [ ] Machine learning for lead scoring

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is created for assessment purposes.

## 👨‍ Author

Jared Ahaza - Software Developer Assessment

---

**Note**: This is a demonstration project built for assessment purposes. For production use, additional security measures, testing, and deployment configurations would be required.