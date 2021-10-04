import uuid
from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class AbstractProduct(models.Model):
    name = models.CharField(max_length=400, db_index=True)
    slug = models.SlugField(
        max_length=200,
        db_index=True,
        null=False,
        unique=True,
        help_text="URL, will appear after you save for the first time",
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
    # additional_fields = models.JSONField(
    #     blank=True,
    #     null=True,
    #     help_text="To add extra fields, you can write a json. Delete the 'null' and start writing!",
    # )
    brand = models.ManyToManyField(
        Brand, related_name="brands", related_query_name="brand"
    )
    supplier = models.ManyToManyField(
        Supplier, related_name="suppliers", related_query_name="supplier"
    )

    PLACE_OF_ORIGIN = ((BD, "Bangladesh"), (CHN, "China"))
    place_of_origin = models.CharField(choices=PLACE_OF_ORIGIN, blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ["updated"]

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
        return f"products/{instance.product.slug}/description/{filename}"
    return f"products/{instance.product.slug}/main/{filename}"


class ProductImage(models.Model):
    image = VersatileImageField(
        upload_to=return_product_image_directory,
        max_length=600,
    )
    alt = models.CharField(max_length=128)
    is_description_image = models.BooleanField(default=False)

    def __str__(self):
        return self.alt
