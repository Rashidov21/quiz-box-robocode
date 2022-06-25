from django.db import models

# Create your models here.


class Contact(models.Model):
    fullname = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.fullname}"
