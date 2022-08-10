from django.db import models

from api.models import BaseModel, Country


class University(BaseModel):
    county = models.ForeignKey(
        Country,
        related_name="country", 
        on_delete=models.CASCADE,
    )
    webpage = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="대학교 사이트 주소"
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        help_text="대학교 이름"
    )


class UniversityPreference(BaseModel):
    university = models.ForeignKey(
        University,
        related_name="university_preference", 
        on_delete=models.CASCADE,
    )
    user_id = models.IntegerField()
    deleted_at = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user_id", "University"],
                name="UC"
            )
        ]

    class Meta:
        abstract = False
