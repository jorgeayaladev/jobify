from core.models import BaseModel
from django.db import models


class ApplicantCareer(BaseModel):
    applicant = models.ForeignKey(
        "users.Applicant", on_delete=models.CASCADE, related_name="applicant_careers"
    )

    career = models.ForeignKey(
        "common.Career", on_delete=models.CASCADE, related_name="career_applicants"
    )

    years_experience = models.PositiveIntegerField(default=0)

    is_primary = models.BooleanField(default=True)

    class Meta:
        unique_together = ("applicant", "career")
        indexes = [
            models.Index(fields=["applicant"]),
            models.Index(fields=["career"]),
        ]

    def __str__(self):
        return f"{self.applicant} - {self.career}"
