from django.db import models

# custom models
class Newsletter(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    newsletter_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class Subscriber(models.Model):
    email = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.email


