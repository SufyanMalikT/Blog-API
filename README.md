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
