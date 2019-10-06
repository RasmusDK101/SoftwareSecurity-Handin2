from django.db import models
from django.core import validators

class NewsletterSignup(models.Model):
    username = models.CharField(max_length = 100, validators=[validators.validate_unicode_slug])
    firstnames = models.CharField(max_length = 100, validators=[validators.validate_unicode_slug])
    lastnames = models.CharField(max_length = 100, validators=[validators.validate_unicode_slug])
    email = models.EmailField()

    def __str__(self):
            return self.email
