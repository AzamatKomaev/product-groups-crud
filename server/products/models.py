from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    seq = models.IntegerField()

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        db_table = 'product_categories'
        verbose_name = 'Product category'
        verbose_name_plural = 'Product categories'


class ProductGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    seq = models.IntegerField()
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        db_table = 'product_groups'
        verbose_name = 'Product group'
        verbose_name_plural = 'Product groups'


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    hidden = models.BooleanField()
    group_id = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
