from core.models import BaseModel
from django.db import models
from django.utils.text import slugify

from .category import Category


class Skill(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="skills/", blank=True, null=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="skills",
        limit_choices_to={"type": "skill"},
    )

    # Nivel de popularidad (útil para ranking/matching)
    popularity = models.PositiveIntegerField(default=0)

    # Estado
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "category"], name="unique_skill_per_category"
            )
        ]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["slug"]),
            models.Index(fields=["popularity"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
