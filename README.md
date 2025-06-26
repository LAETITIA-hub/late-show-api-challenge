# 🌙 Late Show API — Phase 4 Code Challenge

A Flask RESTful API for managing a late-night show's guests, episodes, and appearances.

---

## 🚀 Tech Stack

* Python 3.12
* Flask + Flask-SQLAlchemy + Flask-Migrate
* Flask-JWT-Extended (token-based auth)
* PostgreSQL
* Postman for testing
* GitHub for version control

---

## 📁 Project Structure

```
late-show-api-challenge/
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   ├── appearance.py
│   │   └── user.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   ├── appearance_controller.py
│   │   └── user_controller.py
├── migrations/
├── challenge-4-lateshow.postman_collection.json
├── main.py
├── Pipfile
├── Pipfile.lock
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/LAETITIA-hub/late-show-api-challenge.git
cd late-show-api-challenge
```

### 2. Create Virtual Environment

```bash
pipenv install
pipenv shell
```

### 3. Setup PostgreSQL Database

```bash
sudo -u postgres psql
```

Inside psql:
```sql
CREATE DATABASE late_show_db;
ALTER USER postgres WITH PASSWORD 'newpassword123';
\q
```

Update `server/config.py` if needed:
```python
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:newpassword123@localhost:5432/late_show_db"
```

### 4. Migrate + Seed DB

```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial"
flask db upgrade
python server/seed.py
```

### 5. Run the App

```bash
python main.py
```

App will run at: http://localhost:5000

---

## 🔐 Auth Flow

1. **Register**: `POST /register`
2. **Login**: `POST /login` → returns JWT
3. **Use JWT for protected routes**:
   ```
   Authorization: Bearer <token>
   ```

---

## 📡 API Endpoints

| Method | Route | Auth? | Description |
|--------|-------|-------|-------------|
| POST | `/register` | ❌ | Create user |
| POST | `/login` | ❌ | Login user + return JWT |
| GET | `/guests` | ❌ | List all guests |
| GET | `/episodes` | ❌ | List all episodes |
| GET | `/episodes/<id>` | ❌ | Episode + appearances |
| DELETE | `/episodes/<id>` | ✅ | Delete episode |
| POST | `/appearances` | ✅ | Create appearance |

---

## 📝 Sample Requests & Responses

### Register User
```bash
POST /register
Content-Type: application/json

{
  "username": "testuser",
  "password": "password"
}
```

**Response:**
```json
{
  "message": "User registered successfully"
}
```

### Login
```bash
POST /login
Content-Type: application/json

{
  "username": "testuser",
  "password": "password"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Get Episodes
```bash
GET /episodes
```

**Response:**
```json
[
  {
    "id": 1,
    "date": "2024-01-01",
    "number": 1
  },
  {
    "id": 2,
    "date": "2024-01-02",
    "number": 2
  }
]
```

### Get Episode with Appearances
```bash
GET /episodes/1
```

**Response:**
```json
{
  "id": 1,
  "date": "2024-01-01",
  "number": 1,
  "appearances": [
    {
      "id": 1,
      "rating": 5,
      "guest": {
        "id": 1,
        "name": "Beyoncé",
        "occupation": "Singer"
      }
    }
  ]
}
```

### Create Appearance (Protected)
```bash
POST /appearances
Authorization: Bearer <your-jwt-token>
Content-Type: application/json

{
  "guest_id": 1,
  "episode_id": 2,
  "rating": 4
}
```

**Response:**
```json
{
  "id": 3,
  "rating": 4,
  "guest_id": 1,
  "episode_id": 2
}
```

---

## 🧪 Postman Collection

1. Open Postman
2. Import `challenge-4-lateshow.postman_collection.json`
3. Use the requests in this order:
   - Register
   - Login (copy the token)
   - Send token in Authorization header for protected routes

---

## 🗄️ Database Models

### User
- `id` (Primary Key)
- `username` (Unique)
- `password_hash` (Hashed password)

### Guest
- `id` (Primary Key)
- `name`
- `occupation`
- `appearances` (Relationship)

### Episode
- `id` (Primary Key)
- `date`
- `number`
- `appearances` (Relationship with cascade delete)

### Appearance
- `id` (Primary Key)
- `rating` (1-5 validation)
- `guest_id` (Foreign Key)
- `episode_id` (Foreign Key)

---

## ✅ Submission Checklist

- [x] MVC folder structure
- [x] PostgreSQL used
- [x] Models with relationships and validation
- [x] Token auth implemented
- [x] Working seed file
- [x] All routes tested
- [x] README completed
- [x] Code pushed to GitHub

---

## 📎 GitHub Repo

https://github.com/LAETITIA-hub/late-show-api-challenge.git

---

**Made with ❤️ by [Laetitia Kamangu]**

