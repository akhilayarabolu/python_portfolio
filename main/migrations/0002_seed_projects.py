from django.db import migrations


PROJECTS = [
    {
        "title": "Personal Portfolio Website",
        "short_description": "A responsive Django portfolio with contact form, project showcase, and production-ready deployment setup.",
        "description": (
            "Built a complete personal portfolio using Django templates, a Contact model, "
            "admin management, and a clean responsive UI. The site is configured for SQLite locally "
            "and PostgreSQL on Render with WhiteNoise and Gunicorn."
        ),
        "tech_stack": "Python, Django, HTML, CSS, JavaScript, Bootstrap",
        "github_url": "https://github.com/YOUR_GITHUB_USERNAME/python-portfolio",
        "live_url": "",
        "is_featured": True,
        "display_order": 1,
    },
    {
        "title": "Sales Insights Dashboard",
        "short_description": "Interactive Power BI dashboard for sales trends, product performance, and regional insights.",
        "description": (
            "Designed a business dashboard using cleaned Excel/CSV data. Created KPIs for revenue, "
            "profit, and category performance, with slicers for region and time period to support "
            "clear decision-making."
        ),
        "tech_stack": "Power BI, Excel, Data Analysis, DAX",
        "github_url": "",
        "live_url": "",
        "is_featured": True,
        "display_order": 2,
    },
    {
        "title": "Student Performance Analysis",
        "short_description": "Python data analysis project exploring academic scores, patterns, and visual insights.",
        "description": (
            "Used Pandas and NumPy to clean and explore student performance data. Built charts to "
            "compare scores across subjects and identified factors linked with higher performance."
        ),
        "tech_stack": "Python, Pandas, NumPy, Matplotlib, Excel",
        "github_url": "https://github.com/YOUR_GITHUB_USERNAME/student-performance-analysis",
        "live_url": "",
        "is_featured": True,
        "display_order": 3,
    },
    {
        "title": "Library Management System",
        "short_description": "Django web app for book records, issue/return tracking, and simple admin workflows.",
        "description": (
            "Developed CRUD features for books and members with Django models, forms, and admin. "
            "Focused on clean database design, validation, and a beginner-friendly interface."
        ),
        "tech_stack": "Python, Django, SQLite, HTML, CSS",
        "github_url": "https://github.com/YOUR_GITHUB_USERNAME/library-management-system",
        "live_url": "",
        "is_featured": True,
        "display_order": 4,
    },
]


def seed_projects(apps, schema_editor):
    Project = apps.get_model("main", "Project")
    for item in PROJECTS:
        Project.objects.update_or_create(title=item["title"], defaults=item)


def unseed_projects(apps, schema_editor):
    Project = apps.get_model("main", "Project")
    Project.objects.filter(title__in=[item["title"] for item in PROJECTS]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_projects, unseed_projects),
    ]
