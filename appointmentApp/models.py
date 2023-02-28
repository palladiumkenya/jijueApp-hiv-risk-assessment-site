# Create your models here.

from django.db import models
from django.http import request


# Model for apppointment
class VirtualCounsellor(models.Model):
    name = models.CharField(max_length=256)
    mail = models.EmailField(max_length=256)
    phone_number = models.CharField(max_length=256)
    date_time = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=256)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ["-sent_date"]
