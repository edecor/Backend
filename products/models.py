import uuid
from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=400, db_index=True)
    slug = models.SlugField(
        max_length=200,
        db_index=True,
        null=False,
        unique=True,
        help_text="dw it'll appear after you save the first time",
    )

    categories = models.ManyToManyField(
        Category,
        related_name="categories",
        related_query_name="category",
    )
    description = models.TextField(
        blank=True,
        help_text="To add images, Add description images through the form below first and then insert the url of the image here",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    additional_fields = models.JSONField(
        blank=True,
        null=True,
        help_text="To add extra fields, you can write a json. Delete the 'null' and start writing!",
    )

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(["id", "slug"], name="id_slug_idx")]

    def __str__(self):
        return self.name

    @property
    def image_count(self):
        return self.images.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.uuid}")
        return super().save(*args, **kwargs)


def return_product_image_directory(instance, filename):
    if instance.is_description_image:
        return f"products/{instance.product.slug}-{instance.product.uuid}/description/{filename}"
    return f"products/{instance.product.slug}-{instance.product.uuid}/main/{filename}"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = VersatileImageField(
        upload_to=return_product_image_directory,
        default="default_img.jpg",
        max_length=600,
    )
    alt = models.CharField(max_length=128)
    is_description_image = models.BooleanField(default=False)

    def __str__(self):
        return self.alt


# ------------- MAIN CATEGORY MODELS -------------#

# class MaterialCategory(Product):
