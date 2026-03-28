from core.models import BaseModel
from django.db import models
from django.utils.text import slugify

from .category import Category


class Career(BaseModel):
    name = models.CharField(max_length=150)
    slug = models.SlugField(blank=True)

    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="careers/", blank=True, null=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="careers",
        limit_choices_to={"type": "career"},
    )

    # Nivel de demanda (útil para analítica)
    demand_level = models.CharField(
        max_length=20,
        choices=[
            ("low", "Low"),
            ("medium", "Medium"),
            ("high", "High"),
        ],
        default="medium",
    )

    # Salario referencial (opcional)
    average_salary = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "category"], name="unique_career_per_category"
            )
        ]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["slug"]),
            models.Index(fields=["demand_level"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
