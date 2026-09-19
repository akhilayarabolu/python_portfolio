from django.conf import settings


def site_profile(request):
    return {
        "site_name": settings.SITE_NAME,
        "site_role": settings.SITE_ROLE,
        "site_location": settings.SITE_LOCATION,
        "contact_email": settings.CONTACT_EMAIL,
        "github_url": settings.GITHUB_URL,
        "linkedin_url": settings.LINKEDIN_URL,
        "resume_file_name": settings.RESUME_FILE_NAME,
    }
