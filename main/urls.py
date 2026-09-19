from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("skills/", views.skills, name="skills"),
    path("projects/", views.projects, name="projects"),
    path("resume/", views.resume, name="resume"),
    path("resume/download/", views.download_resume, name="download_resume"),
    path("contact/", views.contact, name="contact"),
]
