# 📝 Blog API (Django REST Framework)

A fully functional **Blog API** built with **Django REST Framework (DRF)** that supports user authentication, blog posting, likes, and comments. Authentication is handled using **JWT tokens** for secure access. The backend uses **PostgreSQL** as the database.  

---

## 🚀 Features
- **User Management**
  - User registration & login
  - Profile update (only owner can edit their profile)
- **Blog System**
  - Create, read, update, delete blog posts
  - Like/unlike blog posts
  - Comment on blog posts
- **Permissions**
  - Custom permissions (users can only update their own profile/posts)
- **Authentication**
  - JWT-based authentication using `djangorestframework-simplejwt`
- **Database**
  - PostgreSQL support

---

## 🛠 Tech Stack
- **Backend:** Django, Django REST Framework  
- **Auth:** JWT (`djangorestframework-simplejwt`)  
- **Database:** PostgreSQL  
- **Others:** Pillow (for images), Django CORS Headers  

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/SufyanMalikT/Blog-API.git
cd Blog-API
```

### 2. Create & activate a virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL
Make sure PostgreSQL is installed and running. Create a database:
```sql
CREATE DATABASE blog_api;
```
Then, set up a .env file in the project root:
.env:
```env
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_NAME=blog_api
DATABASE_USER=your_postgres_user
DATABASE_PASSWORD=your_postgres_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```
And update settings.py (or use python-decouple) to load these values.

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Create a superuser
```bash
python manage.py createsuperuser
```
### 7. Run the deployment server
```bash
python manage.py runserver
```

## 🔑 API Endpoints

| Method | Endpoint                  | Description              | Auth Required |
|--------|---------------------------|--------------------------|---------------|
| POST   | `/api/auth/register/`     | Register new user        | ❌            |
| POST   | `/api/auth/login/`        | Login & get JWT tokens   | ❌            |
| GET    | `/api/profile/`           | Get user profile         | ✅            |
| PUT    | `/api/profile/`           | Update own profile       | ✅ (owner)    |
| GET    | `/api/posts/`             | List all blog posts      | ❌            |
| POST   | `/api/posts/`             | Create a new post        | ✅            |
| GET    | `/api/posts/<id>/`        | Get single post details  | ❌            |
| PUT    | `/api/posts/<id>/`        | Update own post          | ✅ (owner)    |
| DELETE | `/api/posts/<id>/`        | Delete own post          | ✅ (owner)    |
| POST   | `/api/posts/<id>/like/`   | Like/unlike a post       | ✅            |
| POST   | `/api/posts/<id>/comment/`| Add comment to post      | ✅            |
