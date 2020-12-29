from django.core.validators import MinLengthValidator
from django.db import models


class Message(models.Model):
    """Data model for the contact form."""

    name = models.CharField(max_length=50, default=None)
    email = models.EmailField(null=False, blank=False, validators=[MinLengthValidator(1)], default=None)
    subject = models.CharField(max_length=100, null=False, blank=False, validators=[MinLengthValidator(1)], default=None)
    content = models.TextField(max_length=256, null=False, blank=False, validators=[MinLengthValidator(1)], default=None)

    def __str__(self):
        return self.subject
