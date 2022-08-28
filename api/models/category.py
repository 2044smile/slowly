from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    # category = models.ForeignKey('Menu', on_delete=models.CASCADE)

    def __str__(self):
        return f"Category {self.name}"


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f"SubCategory {self.name}"
