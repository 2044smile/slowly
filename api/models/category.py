from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    # category = models.ForeignKey('Menu', on_delete=models.CASCADE)


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)