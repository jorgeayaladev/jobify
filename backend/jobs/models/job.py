from django.db import models
from django.utils.text import slugify

from backend.core.models import BaseModel


class Job(BaseModel):
    JOB_TYPE_CHOICES = (
        ("full_time", "Full Time"),
        ("part_time", "Part Time"),
        ("contract", "Contract"),
        ("internship", "Internship"),
    )

    EXPERIENCE_LEVEL_CHOICES = (
        ("junior", "Junior"),
        ("mid", "Mid"),
        ("senior", "Senior"),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)

    description = models.TextField()
    requirements = models.TextField(blank=True)

    company = models.ForeignKey(
        "companies.Company", on_delete=models.CASCADE, related_name="jobs"
    )

    created_by = models.ForeignKey(
        "users.Admin", on_delete=models.SET_NULL, null=True, related_name="jobs_created"
    )

    # Tipo de trabajo
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)

    # Nivel requerido
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVEL_CHOICES)

    # Ubicación
    location = models.CharField(max_length=255, blank=True)
    is_remote = models.BooleanField(default=False)

    # Salario
    salary_min = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    salary_max = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    is_active = models.BooleanField(default=True)

    # Relaciones M2M (con tablas intermedias)
    skills = models.ManyToManyField(
        "common.Skill", through="jobs.JobSkill", related_name="jobs", blank=True
    )

    certifications = models.ManyToManyField(
        "common.Certification",
        through="jobs.JobCertification",
        related_name="jobs",
        blank=True,
    )

    careers = models.ManyToManyField(
        "common.Career", through="jobs.JobCareer", related_name="jobs", blank=True
    )

    class Meta:
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["slug"]),
            models.Index(fields=["is_active"]),
            models.Index(fields=["experience_level"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
