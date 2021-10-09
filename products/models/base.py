import uuid
from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q


class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

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


def return_product_image_directory(instance, filename):
    if instance.is_description_image:
        return f"products/{instance.content_object.slug}/description/{filename}"
    return f"products/{instance.content_object.slug}/main/{filename}"


class ProductImage(models.Model):

    CONTENT_TYPE_CHOICES = Q(app_label="products", model="material")

    image = VersatileImageField(
        upload_to=return_product_image_directory,
        max_length=600,
    )
    alt = models.CharField(max_length=128)
    is_description_image = models.BooleanField(default=False)

    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, limit_choices_to=CONTENT_TYPE_CHOICES
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.alt


class AbstractProduct(models.Model):
    class Meta:
        abstract = True
        ordering = ["updated"]

    PLACE_OF_ORIGIN = (("BD", "Bangladesh"), ("CHN", "China"))

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
    additional_fields = models.JSONField(
        blank=True,
        null=True,
        help_text="To add extra fields, you can write a json. Delete the 'null' and start writing!",
    )

    # m2m fields
    brand = models.ManyToManyField(
        Brand,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )
    supplier = models.ManyToManyField(
        Supplier,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    place_of_origin = models.CharField(
        max_length=50, choices=PLACE_OF_ORIGIN, blank=True, null=True
    )
    color = models.CharField(max_length=250, blank=True, null=True)

    images = GenericRelation(ProductImage)

    def __str__(self):
        return self.name

    @property
    def image_count(self):
        return self.images.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.uuid}")
        return super().save(*args, **kwargs)
