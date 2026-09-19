from pathlib import Path

from django.conf import settings
from django.contrib import messages
from django.http import FileResponse, Http404
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Project


def _page_meta(title, description):
    return {
        "page_title": title,
        "meta_description": description,
    }


def home(request):
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    context = {
        **_page_meta(
            "Y. Akhila | Python Developer Portfolio",
            "Portfolio of Y. Akhila, a Python Developer and Data Analyst fresher from Ongole, Andhra Pradesh.",
        ),
        "featured_projects": featured_projects,
    }
    return render(request, "home.html", context)


def about(request):
    context = _page_meta(
        "About | Y. Akhila",
        "Learn about Y. Akhila, a B.Tech CSE graduate skilled in Python, SQL, Django, Power BI, and data analysis.",
    )
    return render(request, "about.html", context)


def skills(request):
    skill_groups = [
        {
            "title": "Programming",
            "icon": "bi-code-slash",
            "items": ["Python", "SQL", "Java"],
        },
        {
            "title": "Web Development",
            "icon": "bi-globe2",
            "items": ["Django", "HTML", "CSS", "JavaScript"],
        },
        {
            "title": "Data Analytics",
            "icon": "bi-bar-chart",
            "items": ["Excel", "Power BI", "Tableau", "Pandas", "NumPy"],
        },
        {
            "title": "Machine Learning",
            "icon": "bi-cpu",
            "items": ["Scikit-learn", "Regression", "Classification", "Decision Trees"],
        },
        {
            "title": "Database",
            "icon": "bi-database",
            "items": ["MySQL", "PostgreSQL"],
        },
        {
            "title": "Tools",
            "icon": "bi-tools",
            "items": ["Git", "GitHub", "VS Code"],
        },
    ]
    context = {
        **_page_meta(
            "Skills | Y. Akhila",
            "Technical skills of Y. Akhila including Python, Django, SQL, Power BI, Tableau, and machine learning.",
        ),
        "skill_groups": skill_groups,
    }
    return render(request, "skills.html", context)


def projects(request):
    context = {
        **_page_meta(
            "Projects | Y. Akhila",
            "Python, Django, and data analysis projects by Y. Akhila.",
        ),
        "projects": Project.objects.all(),
    }
    return render(request, "projects.html", context)


def resume(request):
    resume_path = Path(settings.BASE_DIR) / "main" / "static" / "files" / settings.RESUME_FILE_NAME
    context = {
        **_page_meta(
            "Resume | Y. Akhila",
            "Education, skills, projects, and career objective of Y. Akhila, Python Developer and Data Analyst.",
        ),
        "resume_available": resume_path.exists(),
    }
    return render(request, "resume.html", context)


def download_resume(request):
    resume_path = Path(settings.BASE_DIR) / "main" / "static" / "files" / settings.RESUME_FILE_NAME
    if resume_path.exists():
        return FileResponse(
            open(resume_path, "rb"),
            as_attachment=True,
            filename=settings.RESUME_FILE_NAME,
        )
    messages.info(
        request,
        "The resume PDF is not uploaded yet. Please view the Resume page, or add your PDF to main/static/files/.",
    )
    return redirect("resume")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you. Your message has been sent successfully.")
            return redirect("contact")
        messages.error(request, "Please correct the errors below and try again.")
    else:
        form = ContactForm()

    context = {
        **_page_meta(
            "Contact | Y. Akhila",
            "Contact Y. Akhila for Python development, Django, or data analysis opportunities.",
        ),
        "form": form,
    }
    return render(request, "contact.html", context)


def page_not_found(request, exception):
    context = _page_meta(
        "Page not found | Y. Akhila",
        "The requested page could not be found on Y. Akhila's portfolio.",
    )
    return render(request, "404.html", context, status=404)
