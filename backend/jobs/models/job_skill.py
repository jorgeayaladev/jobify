from django.db import models

from backend.core.models import BaseModel


class JobSkill(BaseModel):
    job = models.ForeignKey(
        "jobs.Job", on_delete=models.CASCADE, related_name="job_skills"
    )

    skill = models.ForeignKey(
        "common.Skill", on_delete=models.CASCADE, related_name="skill_jobs"
    )

    REQUIRED_LEVEL_CHOICES = (
        ("basic", "Basic"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    )

    required_level = models.CharField(max_length=20, choices=REQUIRED_LEVEL_CHOICES)

    is_mandatory = models.BooleanField(default=True)

    class Meta:
        unique_together = ("job", "skill")
        indexes = [
            models.Index(fields=["job"]),
            models.Index(fields=["skill"]),
        ]

    def __str__(self):
        return f"{self.job} - {self.skill}"
