from twilio.rest import Client
from django.db import models
from django.http import request

# Create your models here.


class PredResults(models.Model):
    age = models.PositiveBigIntegerField()
    gender = models.PositiveBigIntegerField()
    county = models.CharField(max_length=100)
    maritalStatus = models.PositiveBigIntegerField()
    coupleDiscordant = models.PositiveBigIntegerField()
    SexWithWoman = models.CharField(max_length=256)
    SexWithMan = models.CharField(max_length=256)
    condom_use = models.CharField(max_length=256)
    sw = models.PositiveBigIntegerField()
    pwid = models.PositiveBigIntegerField()
    testedBefore = models.PositiveBigIntegerField()
    presumedTB = models.PositiveBigIntegerField()
    treatmentTB = models.PositiveBigIntegerField()
    sti = models.CharField(max_length=100)
    rapevictim = models.CharField(max_length=100)
    HIVPrEP = models.CharField(max_length=100)
    y_pred = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.y_pred


# sent results model
class resultMail(models.Model):
    email = models.CharField(max_length=256)
    result = models.CharField(max_length=256)
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# Model for apppointment

class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ["-sent_date"]


# Message Handling Model


class Message(models.Model):
    name = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        account_sid = 'AC70ddd96f0b8b5d27828a2f9b8b34f125'
        auth_token = 'fcd66ee758cbb2887f934dbaa4f96437'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"Dear {self.name}, we would like to invite you for free HIV risk assessment. Kindly visit our site https://jijue.com",
            from_='+13853965642',
            to={self.phonenumber}
        )

        print(message.sid)
        return super().save(*args, **kwargs)
