from django.conf import settings
from django.db import models

from backend.core.models import BaseModel


class Admin(BaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="admin"
    )

    company = models.ForeignKey(
        "companies.Company", on_delete=models.CASCADE, related_name="admins"
    )

    position = models.CharField(max_length=255, blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=["company"]),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.company.name}"
