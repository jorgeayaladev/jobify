from core.models import BaseModel
from django.db import models


class JobCareer(BaseModel):
    job = models.ForeignKey(
        "jobs.Job", on_delete=models.CASCADE, related_name="job_careers"
    )

    career = models.ForeignKey(
        "common.Career", on_delete=models.CASCADE, related_name="career_jobs"
    )

    is_primary = models.BooleanField(default=True)

    class Meta:
        unique_together = ("job", "career")
        indexes = [
            models.Index(fields=["job"]),
            models.Index(fields=["career"]),
        ]

    def __str__(self):
        return f"{self.job} - {self.career}"
