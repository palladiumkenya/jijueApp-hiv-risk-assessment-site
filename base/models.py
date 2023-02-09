from twilio.rest import Client
from django.db import models
from django.http import request

from dotenv import load_dotenv
import os
load_dotenv()

# Create your models here.


class PredictedResult(models.Model):
    user_id = models.AutoField(primary_key=True)
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

# Contact form model


class ContactMessage(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    message = models.CharField(max_length=512)
    sent_date = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.name

# sent results model


class resultMail(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    result = models.CharField(max_length=256)
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# Message Handling Model


class ReferralMessage(models.Model):
    name = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        account_sid = os.environ.get('account_sid')
        auth_token = os.environ.get('auth_token')
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"Dear {self.name}, we would like to invite you for free HIV risk assessment. Kindly visit our site https://jijue.com",
            from_='+13853965642',
            to={self.phonenumber}
        )

        print(message.sid)
        return super().save(*args, **kwargs)
