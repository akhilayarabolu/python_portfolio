from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact message"
        verbose_name_plural = "Contact messages"

    def __str__(self):
        return f"{self.name} — {self.subject}"


class Project(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=280)
    description = models.TextField()
    tech_stack = models.CharField(
        max_length=300,
        help_text="Comma-separated technologies, for example: Python, Django, SQL",
    )
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "title"]

    def __str__(self):
        return self.title

    def tech_list(self):
        return [item.strip() for item in self.tech_stack.split(",") if item.strip()]
