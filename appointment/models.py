from django.db import models

# Create your models here.


class County(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class SubCounty(models.Model):
    name = models.CharField(max_length=128)
    county = models.ForeignKey(
        County, on_delete=models.CASCADE, related_name='subcounties')

    def __str__(self):
        return self.name


class Ward(models.Model):
    name = models.CharField(max_length=128)
    subcounty = models.ForeignKey(
        SubCounty, on_delete=models.CASCADE, related_name='wards')

    def __str__(self):
        return self.name


class Facility(models.Model):
    name = models.CharField(max_length=128)
    ward = models.ForeignKey(
        Ward, on_delete=models.CASCADE, related_name='facilities')

    def __str__(self):
        return self.name
