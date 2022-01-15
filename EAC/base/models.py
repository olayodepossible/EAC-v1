from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Topic(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(BaseModel):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)  # null = false by default
    description = models.TextField(null=True, blank=True)
    # participant =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


# Message Model with One(Room)-to-Many relationship
class Message(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]  # just return max of 50

