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

## Quick start ✅

1. Install Python (3.10+ recommended) and Git.
2. Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

   - Current dependencies:
     - `Django==5.2.8`
     - `Pillow` (required for `ImageField`)

4. Apply migrations and create a superuser:

   ```powershell
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. Run the dev server:

   ```powershell
   python manage.py runserver
   ```

6. Open:

   - Admin: `http://127.0.0.1:8000/admin/` (manage cars/brands)
   - Cars list: `http://127.0.0.1:8000/cars/`

---

## Media & static files 🔧

- Uploaded images are stored in `media/cars/`.
- `MEDIA_ROOT` and `MEDIA_URL` are set in `app/settings.py`. The project serves media files during development via `app/urls.py`.
- If you want to persist media in production, configure external storage (S3, etc.) or use Git LFS for tracked files.

---

## Migrations & history 🧾

- Migrations included in `cars/migrations/` (e.g., `0003_car_image_car_plate.py` adds `image` and `plate` fields to `Car`).
- If you modify models, run `python manage.py makemigrations` and `python manage.py migrate`.

---

## Templates & UI

- `cars/templates/cars.html` – list with search and card grid (uses Tailwind CDN).
- `cars/templates/details.html` – detailed view with large image and actions.
- Dark mode is implemented by toggling a `dark` class on `<html>` and saving the preference in `localStorage`.

---

## Notes & best practices ⚠️

- The `SECRET_KEY` in `app/settings.py` is for development only. Use environment variables for production secrets.
- `db.sqlite3` and `media/` are present locally; consider ignoring or using external storage in production.
- To add sample data quickly, use the Django admin or write fixtures.

---

## Git / GitHub

If you'd like help pushing this repo to GitHub, I can guide you through or automate the steps (create a repo, set remote, push). Tell me if you want it **public** or **private** and the repo name.

---

> If you'd like, I can add a short CONTRIBUTING or DEVELOPMENT section next (tests, CI, or Docker setup). 💡

