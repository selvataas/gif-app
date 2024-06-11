from django.db import models
from django.conf import settings


class Image(models.Model):
    title = models.CharField(max_length=60, blank=False)
    image = models.ImageField(max_length=36)
    uploaded_date = models.DateTimeField()
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'Image<{self.id}>'