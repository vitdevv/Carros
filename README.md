# Carros (Django)

A simple Django app to list cars with images, brands, and details. Includes a Tailwind-based frontend and dark-mode toggle.

## Quick start

1. Install Python (3.10+ recommended) and Git.
2. Create and activate a virtual environment:

   python -m venv venv
   venv\Scripts\activate  # Windows

3. Install dependencies:

   pip install -r requirements.txt

4. Run migrations and start server:

   python manage.py migrate
   python manage.py runserver

5. Open http://127.0.0.1:8000/cars/ in your browser.

## Add to Git and push to GitHub

If you want me to do this automatically, please install Git and (optionally) the GitHub CLI (`gh`) and tell me whether you want the repo **public** or **private**, and the repository name.

Manual steps (once Git is installed):

```bash
# Configure git (only once)
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Initialize repo and commit
cd /path/to/Carros
git init
git add .
git commit -m "Initial commit"

# Create remote repository on GitHub (option 1: use website)
# - Create a new repo on GitHub (do NOT initialize with README)
# - Then:
# git remote add origin https://github.com/<your-username>/<repo>.git
# git branch -M main
# git push -u origin main

# (option 2: use GitHub CLI)
# gh repo create <repo-name> --public --source=. --remote=origin --push
```

## Notes

- `db.sqlite3` and `media/` are ignored by default. If you need media files versioned, consider using Git LFS or external storage.
- SECRET_KEY in `app/settings.py` is for development only. Use environment variables in production.

