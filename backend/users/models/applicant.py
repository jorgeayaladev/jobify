from django.conf import settings
from django.db import models

from backend.core.models import BaseModel


class Applicant(BaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="applicant"
    )

    phone = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    resume = models.FileField(upload_to="resumes/", null=True, blank=True)
    linkedin_url = models.URLField(blank=True)

    location = models.CharField(max_length=255, blank=True)

    is_available = models.BooleanField(default=True)

    # Relaciones M2M con tablas intermedias
    skills = models.ManyToManyField(
        "common.Skill",
        through="users.ApplicantSkill",
        related_name="applicants",
        blank=True,
    )

    certifications = models.ManyToManyField(
        "common.Certification",
        through="users.ApplicantCertification",
        related_name="applicants",
        blank=True,
    )

    careers = models.ManyToManyField(
        "common.Career",
        through="users.ApplicantCareer",
        related_name="applicants",
        blank=True,
    )

    class Meta:
        indexes = [
            models.Index(fields=["is_available"]),
            models.Index(fields=["location"]),
        ]

    def __str__(self):
        return self.user.username
