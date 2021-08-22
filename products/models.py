from django.db import models
from versatileimagefield.fields import VersatileImageField


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=400, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    categories = models.ManyToManyField(
        Category,
        related_name="categories",
        related_query_name="category",
    )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(["id", "slug"], name="id_slug_idx")]

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = VersatileImageField(upload_to="products", blank=True, null=True)
    alt = models.CharField(max_length=128)

    def __str__(self):
        return self.alt
