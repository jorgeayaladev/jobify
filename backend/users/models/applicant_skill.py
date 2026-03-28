from django.db import models

from backend.core.models import BaseModel


class ApplicantSkill(BaseModel):
    applicant = models.ForeignKey(
        "users.Applicant", on_delete=models.CASCADE, related_name="applicant_skills"
    )

    skill = models.ForeignKey(
        "common.Skill", on_delete=models.CASCADE, related_name="skill_applicants"
    )

    LEVEL_CHOICES = (
        ("basic", "Basic"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    )

    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

    years_experience = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("applicant", "skill")
        indexes = [
            models.Index(fields=["applicant"]),
            models.Index(fields=["skill"]),
        ]

    def __str__(self):
        return f"{self.applicant} - {self.skill}"
