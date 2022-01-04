import uuid

from django.db import models
from django.utils.text import slugify

from rooms.models import Room


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


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

    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    rooms = models.ManyToManyField(Room)

    place_of_origin = models.CharField(
        max_length=50, choices=PLACE_OF_ORIGIN, blank=True, null=True
    )
    color = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.uuid}")
        return super().save(*args, **kwargs)
