from django.db import models

from api.models import BaseModel


class Country(models.Model):
    code = models.CharField(
        max_length=2,
        blank=True,
        null=True,
        help_text="국가 2자리 코드"
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="국가 영문 이름"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.code

    class Meta:
        abstract = False
