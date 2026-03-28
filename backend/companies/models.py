from core.models import BaseModel
from django.db import models


# Create your models here.
class Company(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name
