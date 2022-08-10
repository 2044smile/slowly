from django.db import models

from api.models import BaseModel


class Country(BaseModel):
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

    def __str__(self):
        return self.code