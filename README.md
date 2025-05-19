
---

```markdown
# 🛡️ JWT Authenticated WebSocket Chat

A real-time chat application built with **Django**, **Django Channels**, **WebSocket**, and **JWT authentication**. This project demonstrates secure, token-based, real-time communication using PostgreSQL as the database.

## 📌 Features

- 🔐 **JWT Authentication** using `djangorestframework-simplejwt`
- 📡 **Real-time chat** with `WebSocket` and `Django Channels`
- 👥 Only **authenticated users** can send messages
- 🗃️ Messages stored in **PostgreSQL** using Django ORM
- 🚫 Unauthorized users are redirected to login
- 🔄 Token passed via WebSocket query string for secure validation

## 🧰 Tech Stack

- **Backend**: Django, Django REST Framework, Django Channels
- **Authentication**: JWT (JSON Web Tokens)
- **Frontend**: HTML, Vanilla JS (`chat_script.js`)
- **Database**: PostgreSQL
- **WebSocket Middleware**: Custom JWT token validation middleware

## 🏗️ Architecture Overview

```

\[Browser]
|
\[WebSocket + JWT Token]
|
\[JWT Middleware → ChatConsumer]
|
\[Channel Layer]
|
\[PostgreSQL → Message\_Chat]

````

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/mahdiabbasi3/jwt-chat-app.git
cd jwt-chat-app
````

### 2. Set up virtualenv

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL settings

In `settings.py`, update your `DATABASES` config:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

### 7. Start chatting!

* Go to `/login_page/` to log in
* POST your credentials to `/api/login/` to receive a JWT token
* Authenticated users can now use the chat in real-time

## 📂 Key Files Overview

* `chat_script.js` – Handles WebSocket logic on the client-side
* `consumers.py` – Main socket event handler
* `jwt_middlewere.py` – Custom JWT validation middleware for WebSocket
* `models.py` – `Message_Chat` model definition
* `views.py` – JWT login API and chat view
* `routing.py` – WebSocket URL routes

## 🧪 WebSocket Payloads

**Client → Server:**

```json
{ "message": "Hello world!" }
```

**Server → Client:**

```json
{ "user": "john_doe", "message": "Hello world!" }
```

## 🪪 License

MIT License

---

## ✨ Author

Made with ❤️ by [mahdi abbasi](https://github.com/mahdiabbasi3)

```

---

