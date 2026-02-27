# 🚀 Django Allauth Boilerplate

An authentic, production-ready Django boilerplate featuring a custom UUID-based User model, integrated Multi-Factor Authentication (MFA), and a modular Bootstrap 5 UI for all authentication flows.

---

## ✨ Key Features

### 🔐 Custom User Model
- Built using UUID for primary keys
- Includes fields for phone number verification

### 🔗 Django-Allauth Suite
- Pre-configured for Social Accounts (Google, GitHub, Facebook, etc.)
- Multi-Factor Authentication support:
  - TOTP (Time-based One-Time Password)
  - WebAuthn

### ⚙️ Modular Settings
- Split into:
  - `base.py`
  - `local.py`
  - `production.py`
- Enables environment-specific configuration

### 🎨 Enhanced UI
- Custom allauth templates
- Built using a modern **Element/Layout architecture**
- Easy branding and customization

### ⚡ Smart Initialization
- Includes `setup_project.py` script to:
  - Rename the project
  - Generate a secure `SECRET_KEY`

---

## 📂 Project Structure

The project follows a clean **Config/Apps separation**:

```plaintext
regular-django/
├── apps/                 # Business logic and custom apps
│   ├── core/             # Global tools (context processors, etc.)
│   └── users/            # Custom User model & Allauth adapters
├── config/               # Project-wide settings and entry points
│   ├── settings/         # Base, Local, Production settings
│   ├── urls.py           # Main routing
│   └── wsgi/asgi.py      # Server gateways
├── templates/            # Global HTML templates and UI elements
├── .env                  # Environment variables
├── manage.py             # Django management script
└── setup_project.py      # One-click initializer
```


## 🛠️ Quick Start

### 1. Clone the Repository

```
git clone https://github.com/Abd0uk/django-allauth-boilerplate.git my-new-project
cd my-new-project
```

---

### 2. Initialize the Project

Run the automated script:

```bash
python setup_project.py
```

This will:

* Set your project name
* Generate a unique `SECRET_KEY`

---

### 3. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

---

### 4. Database Setup

Default database is SQLite:

```bash
python manage.py migrate
python manage.py createsuperuser
```

---

### 5. Run the Server

```bash
python manage.py runserver
```

---

## ⚙️ Environment Configuration

Your `.env` file controls the core behavior:

| Variable      | Description                                     |
| ------------- | ----------------------------------------------- |
| DEBUG         | `True` for development, `False` for production  |
| SECRET_KEY    | Generated automatically by `setup_project.py`   |
| ALLOWED_HOSTS | Comma-separated domains                         |
| DATABASE_URL  | Database connection string (defaults to SQLite) |

---

## 🧑‍💻 Customizing the UI

To customize the design, edit:

```plaintext
templates/allauth/elements/
```

These reusable elements (buttons, inputs, forms) are used across all authentication pages, ensuring a consistent Bootstrap 5 theme.
