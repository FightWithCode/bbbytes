from django.db import models
from django.core.validators import RegexValidator


class Query(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
	
    def __str__(self):
        return str(self.name + ' | ' + self.title)


class NewsLetter(models.Model):
    email = models.CharField(max_length=100)
    unsubscribed = models.BooleanField(default=False)

    def __str__(self):
        return self.email
