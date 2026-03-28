from django.db import models
from django.utils.text import slugify

from backend.core.models import BaseModel

from .category import Category


class Certification(BaseModel):
    name = models.CharField(max_length=150)
    slug = models.SlugField(blank=True)

    issuing_organization = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="certifications/", blank=True, null=True)
    description = models.TextField(blank=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="certifications",
        limit_choices_to={"type": "certification"},
    )

    # Agrega un campo para marcar si la certificación está activa o no
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "category"], name="unique_certification_per_category"
            )
        ]
        indexes = [
            models.Index(fields=["name"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
