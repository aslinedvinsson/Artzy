from django.db import models
import uuid


# custom model
class Newsletter(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    newsletter_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


# custom model
class Subscriber(models.Model):
    email = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=50)
    identifier = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.email
