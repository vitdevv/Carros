# Carros (Django) 🚗

A small Django project to browse and view cars with images, brands, and details. Features a TailwindCSS-based frontend with a persistent dark-mode toggle, search, and image uploads (served from `media/` during development).

---

## 🚀 Features

- Django project with a `cars` app (models, views, templates, admin).
- Models:
  - `Brand` (name)
  - `Car` (model, `brand` FK, `factory_year`, `model_year`, `plate`, `value`, `image`)
- Image uploads handled by Django `ImageField` (uploads to `media/cars/`). Requires `Pillow`.
- Responsive UI built with Tailwind (CDN) and a JavaScript dark-mode toggle persisted in `localStorage`.
- Search on the cars list via `?search=` query parameter.
- Admin configured (`/admin/`) with `Car` and `Brand` registered and searchable.
- URL endpoints:
  - `GET /cars/` → cars list (template `cars.html`, URL name `cars_list`)
  - `GET /cars/<id>/` → car detail (template `details.html`, URL name `car_details`)

---

# Carros — Django car catalog

A small Django app to browse cars with images, brands, and details. Intended for local development and demonstration purposes.

## Quick start

Prerequisites: Python 3.10+, Git

1. Create and activate a virtual environment (Windows):

```powershell
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Apply migrations and create a superuser:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4. Run the development server:

```powershell
python manage.py runserver
```

Visit the admin at `http://127.0.0.1:8000/admin/` and the cars list at `http://127.0.0.1:8000/cars/`.

## What’s included

- `cars` app: models, views, templates and admin registration
- Image uploads via `ImageField` (stored in `media/cars/`) — requires `Pillow`
- Simple search on the list view (`?search=`)
- Tailwind-based responsive templates in `cars/templates/`

## Media & settings

- Development media are stored under the `media/` folder. `MEDIA_ROOT` and `MEDIA_URL` are configured in `app/settings.py`.
- For production, configure external storage (S3, etc.) and set secret/config values via environment variables.

## Migrations

- Migration files are in `cars/migrations/`. When changing models run:

```powershell
python manage.py makemigrations
python manage.py migrate
```

## Tests

Run the test suite with:

```powershell
python manage.py test
```

## Notes

- `db.sqlite3` is for local development only.
- Keep `SECRET_KEY` and other secrets out of source control; use environment variables for production.

## Next steps

If you want, I can add a `CONTRIBUTING.md`, Docker setup, or CI workflow. I can also help push this repository to GitHub.

---

## Full README (expanded)

### Project overview

`Carros` is a small Django project demonstrating a simple catalog of cars with image uploads, searchable list views, and a detail page. It is designed for learning, prototyping, and small demos.

### Features

- Browse cars with brand, year, plate, value and image
- Upload images via Django `ImageField` (stores in `media/cars/` during development)
- Search the list (`?search=`)
- Admin interface to manage `Brand` and `Car`
- Tailwind-based responsive frontend with a small dark-mode toggle stored in `localStorage`

### Repository layout

- `app/` — Django project settings and URLs
- `cars/` — main app (models, views, forms, templates, tests)
- `media/` — uploaded images (development)
- `db.sqlite3` — local SQLite database (development)

### Prerequisites

- Python 3.10+ (3.11 recommended)
- Git
- `pip` and virtual environment support
- `Pillow` for image handling (installed via `requirements.txt`)

### Environment & configuration

The project uses settings in `app/settings.py`. Important configuration items to set for production:

- `SECRET_KEY` — keep secret (use environment variable)
- `DEBUG` — set to `False` in production
- `ALLOWED_HOSTS` — list of hostnames
- `DATABASES` — default is SQLite for development; configure Postgres or another RDBMS for production
- `MEDIA_ROOT` and `MEDIA_URL` — where uploaded files are stored and served from
- Storage backend — for production media use S3 or similar

Example using environment variables (recommended pattern):

```py
import os

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-secret')
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '127.0.0.1').split(',')
```

### Install and run (development)

1. Create and activate a virtualenv:

```powershell
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Apply database migrations and create a superuser:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4. (Optional) Load fixtures or create sample data via admin.

5. Run the development server:

```powershell
python manage.py runserver
```

6. Visit:

- Admin: `http://127.0.0.1:8000/admin/`
- Cars list: `http://127.0.0.1:8000/cars/`

### Serving media in development

When `DEBUG=True` the project serves media files using `django.conf.urls.static` in `app/urls.py`. Uploaded files are written to the `media/` folder.

### Tests

Run the test suite:

```powershell
python manage.py test
```

Add tests to `cars/tests.py` for views, forms and models as needed.

### Docker (optional)

Below is a minimal Docker setup you can adopt; create a `Dockerfile` and `docker-compose.yml` if you'd like.

Minimal `Dockerfile` example:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONUNBUFFERED=1
CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]
```

`docker-compose.yml` snippet (Postgres example):

```yaml
version: '3.8'
services:
  web:
    build: .
    command: gunicorn app.wsgi:application --workers 2 --bind 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    env_file: .env
    depends_on:
      - db
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: carro_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:
```

Notes: If you use Docker for development, mount the `media/` directory and load static files appropriately.

### Deployment notes

- Use a production WSGI server such as `gunicorn` behind Nginx.
- Serve static files with WhiteNoise or via CDN (CloudFront) after `collectstatic`.
- Store user uploads in durable object storage (S3) and use signed URLs or a CDN for serving.
- Configure secure headers, CORS and HTTPS on your front-facing server.

### Security checklist

- Do not commit `SECRET_KEY` or other secrets to source control.
- Use HTTPS in production.
- Keep dependencies up to date.
- Validate and sanitize user-provided file uploads; keep `Pillow` updated.

### Contributing

Contributions are welcome. Suggested next steps I can add for you:

- `CONTRIBUTING.md` with contribution guidelines and code style
- Pre-commit hooks (black, isort, flake8)
- Basic CI workflow to run tests on PRs

Tell me which of the above you want me to add and I will create the files.

### License

Add your license of choice. If you don't have one, I can add an MIT or Apache-2.0 license file for you.

---

If you'd like I can also:

- Create `CONTRIBUTING.md` and `.github/workflows/ci.yml` to run tests
- Add a `Dockerfile` and `docker-compose.yml` and verify locally
- Push the repo to GitHub and create an initial release

Tell me which of those you'd like next.


