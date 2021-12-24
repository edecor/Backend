from django.db import models


# class RoomProducts(models.Manager):
#     def get_queryset(self):
#         mat_qset = Room.material


class Room(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
