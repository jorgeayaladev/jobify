from django.db import models

from backend.core.models import BaseModel


class ApplicantCertification(BaseModel):
    applicant = models.ForeignKey(
        "users.Applicant",
        on_delete=models.CASCADE,
        related_name="applicant_certifications",
    )

    certification = models.ForeignKey(
        "common.Certification",
        on_delete=models.CASCADE,
        related_name="certification_applicants",
    )

    issue_date = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)

    credential_id = models.CharField(max_length=255, blank=True)
    credential_url = models.URLField(blank=True)

    is_verified = models.BooleanField(default=False)

    class Meta:
        unique_together = ("applicant", "certification")
        indexes = [
            models.Index(fields=["applicant"]),
            models.Index(fields=["certification"]),
        ]

    def __str__(self):
        return f"{self.applicant} - {self.certification}"
