# Y. Akhila — Python Developer Portfolio

A complete Django portfolio website for **Y. Akhila**, a Python Developer / Data Analyst fresher from Ongole, Andhra Pradesh, India. The project is ready for local development with SQLite and production deployment on Render with PostgreSQL, Gunicorn, and WhiteNoise.

## 1. Project overview

This website presents a professional profile, skills, projects, resume content, and a working contact form. Messages submitted through the contact page are stored in the database and can be reviewed in Django admin.

## 2. Features

- Responsive Home, About, Skills, Projects, Resume, and Contact pages
- Modern developer-themed hero section without requiring an external photo
- Skill cards grouped by category
- Project cards that can be edited in Django admin
- Working contact form with validation and database storage
- Django admin for contact messages and projects
- Custom 404 page
- Favicon, SEO title, and meta description
- Resume download that works as soon as you add a PDF
- Production settings using environment variables
- Render build files: `requirements.txt`, `build.sh`, and `render.yaml`

## 3. Technologies

- Python 3
- Django
- HTML5, CSS3, JavaScript
- Bootstrap 5
- SQLite (local)
- PostgreSQL (Render)
- Gunicorn
- WhiteNoise
- Git / GitHub
- Render

## 4. Folder structure

```text
python_portfolio/
├── manage.py
├── portfolio/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   ├── static/
│   │   ├── css/style.css
│   │   ├── js/script.js
│   │   ├── images/favicon.svg
│   │   └── files/          # add Y_Akhila_Resume.pdf here
│   └── templates/
├── media/
├── requirements.txt
├── build.sh
├── render.yaml
├── Procfile
├── runtime.txt
├── .env.example
├── .gitignore
└── README.md
```

## 5. How to install Python

1. Download Python 3 from [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. During installation on Windows, check **Add python.exe to PATH**.
3. Confirm the install:

```bash
python --version
```

## 6. How to create a virtual environment

Open a terminal in the project folder:

```bash
cd D:\python_portfolio
python -m venv .venv
```

## 7. How to activate the virtual environment on Windows

PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

Command Prompt:

```bat
.venv\Scripts\activate.bat
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate again.

## 8. How to install requirements

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 9. How to run migrations

```bash
python manage.py migrate
```

## 10. How to create a superuser

```bash
python manage.py createsuperuser
```

Use this account to log in at `/admin/` and view contact messages or edit project links.

## 11. How to run locally

1. Copy environment values:

```bash
copy .env.example .env
```

2. Edit `.env` and replace GitHub, LinkedIn, and email values.
3. Run the server:

```bash
python manage.py runserver
```

4. Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

Useful checks:

```bash
python manage.py check
python manage.py test
```

On Windows, Gunicorn is not used locally. Gunicorn is for Render (Linux). Local development uses `runserver`.

## 12. How to create a GitHub repository

1. Sign in to GitHub.
2. Click **New repository**.
3. Name it, for example `python-portfolio`.
4. Keep it empty (do not add a README, .gitignore, or license, because this project already has them).
5. Create the repository and copy the HTTPS URL.

## 13. How to push the project to GitHub

```bash
cd D:\python_portfolio
git init
git add .
git commit -m "Add Django portfolio website"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/python-portfolio.git
git push -u origin main
```

Replace `YOUR_GITHUB_USERNAME` and the repository name with your values.

## 14. How to deploy to Render

### Option A — Blueprint (`render.yaml`)

1. Push the project to GitHub.
2. Open [https://dashboard.render.com/](https://dashboard.render.com/).
3. Click **New +** → **Blueprint**.
4. Connect the GitHub repository.
5. Apply the Blueprint. Render will create the web service and PostgreSQL database from `render.yaml`.
6. After the first deploy, open the service and confirm the public URL.

### Option B — Manual Web Service

1. In Render, create a **PostgreSQL** database and copy the **Internal Database URL**.
2. Create a **Web Service** from the GitHub repo.
3. Use these settings:
   - **Runtime:** Python
   - **Build Command:** `chmod +x build.sh && ./build.sh`
   - **Start Command:** `gunicorn -c gunicorn.conf.py portfolio.wsgi:application`
4. Add the environment variables listed below.
5. Deploy.

The build command installs packages, collects static files, and runs migrations.

## 15. Render environment variables

Set these on the Web Service:

| Variable | Example | Required |
| --- | --- | --- |
| `SECRET_KEY` | a long random string | Yes |
| `DEBUG` | `False` | Yes |
| `ALLOWED_HOSTS` | `.onrender.com,your-service.onrender.com` | Yes |
| `DATABASE_URL` | Render PostgreSQL URL | Yes in production |
| `SECURE_SSL_REDIRECT` | `True` | Recommended |
| `GITHUB_URL` | your GitHub profile URL | Recommended |
| `LINKEDIN_URL` | your LinkedIn profile URL | Recommended |
| `CONTACT_EMAIL` | your email | Recommended |
| `CSRF_TRUSTED_ORIGINS` | `https://your-service.onrender.com` | If form submit fails |
| `RESUME_FILE_NAME` | `Y_Akhila_Resume.pdf` | Optional |

Render also provides `RENDER_EXTERNAL_HOSTNAME`, which this project adds to `ALLOWED_HOSTS` automatically.

Never commit a real production `SECRET_KEY`.

## 16. How to connect PostgreSQL

Locally, Django uses SQLite automatically when `DATABASE_URL` is not set.

On Render:

1. Create a PostgreSQL instance.
2. Copy the connection string.
3. Set it as `DATABASE_URL` on the web service.
4. Redeploy so `python manage.py migrate` runs against PostgreSQL.

`render.yaml` already wires `DATABASE_URL` from the `portfolio-db` database.

If Render's free database plan is unavailable, create any Render PostgreSQL instance you have access to and paste its URL into `DATABASE_URL`.

## 17. How to update the deployed website

1. Change files locally.
2. Test:

```bash
python manage.py check
python manage.py runserver
```

3. Commit and push:

```bash
git add .
git commit -m "Update portfolio content"
git push
```

4. Render will rebuild automatically if auto-deploy is enabled.
5. After deploy, confirm:
   - Home and inner pages load
   - Static CSS/JS load
   - Contact form saves a message
   - `/admin/` works with your superuser

To create a superuser on Render, open the service **Shell** and run:

```bash
python manage.py createsuperuser
```

## Values you should replace

Replace these before sharing the site:

- `GITHUB_URL` in `.env`, `render.yaml`, and Django admin project links
- `LINKEDIN_URL`
- `CONTACT_EMAIL`
- Project GitHub / live URLs in **Admin → Projects**
- Resume PDF: add `main/static/files/Y_Akhila_Resume.pdf`
- Certification details in `main/templates/resume.html`

## Django admin

- URL: `/admin/`
- Contact messages: **Contact messages**
- Project links: **Projects**

Mark a contact message as read with the `is_read` checkbox.

## License

This project is personal portfolio code for Y. Akhila.
