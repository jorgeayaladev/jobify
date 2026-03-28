from core.models import BaseModel
from django.db import models
from django.utils.text import slugify


class Category(BaseModel):
    CATEGORY_TYPE = (
        ("skill", "Skill"),
        ("certification", "Certification"),
        ("career", "Career"),
    )

    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    type = models.CharField(max_length=20, choices=CATEGORY_TYPE)

    image = models.ImageField(upload_to="categories/", blank=True, null=True)
    description = models.TextField(blank=True)

    # Agrega un campo para marcar si la categoría está activa o no
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "type"], name="unique_category_per_type"
            )
        ]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["slug"]),
            models.Index(fields=["type"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.type}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.type})"
