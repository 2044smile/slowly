from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sub_category = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    # label = models.ManyToManyField('Label', through='ProductLabel')

    def __str__(self):
        return f"Product {self.name}"
