from django.test import TestCase
from django.urls import reverse

from main.models import Contact, Project


class PortfolioPagesTests(TestCase):
    def test_core_pages_load(self):
        for name in ["home", "about", "skills", "projects", "resume", "contact"]:
            response = self.client.get(reverse(name))
            self.assertEqual(response.status_code, 200)

    def test_404_page(self):
        response = self.client.get("/this-page-does-not-exist/")
        self.assertEqual(response.status_code, 404)

    def test_contact_form_saves_message(self):
        response = self.client.post(
            reverse("contact"),
            {
                "name": "Hiring Manager",
                "email": "hiring@example.com",
                "subject": "Python intern role",
                "message": "We would like to discuss an internship opportunity with you.",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Contact.objects.count(), 1)

    def test_project_model(self):
        project = Project.objects.create(
            title="Demo",
            short_description="Short",
            description="Longer description",
            tech_stack="Python, Django",
        )
        self.assertEqual(project.tech_list(), ["Python", "Django"])
