from core.models import BaseModel
from django.db import models


class JobCertification(BaseModel):
    job = models.ForeignKey(
        "jobs.Job", on_delete=models.CASCADE, related_name="job_certifications"
    )

    certification = models.ForeignKey(
        "common.Certification",
        on_delete=models.CASCADE,
        related_name="certification_jobs",
    )

    is_mandatory = models.BooleanField(default=True)

    class Meta:
        unique_together = ("job", "certification")
        indexes = [
            models.Index(fields=["job"]),
            models.Index(fields=["certification"]),
        ]

    def __str__(self):
        return f"{self.job} - {self.certification}"
