from django.db import models
from django.core import validators

class NewsletterSignup(models.Model):
    username = models.CharField(max_length = 100, validators=[validators.validate_slug])
    firstnames = models.CharField(max_length = 100, validators=[validators.validate_slug])
    lastnames = models.CharField(max_length = 100, validators=[validators.validate_slug])
    email = models.EmailField(validators=[validators.validate_email])

    def __str__(self):
            return self.email
