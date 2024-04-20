from django.db import models


class CustomerProfile(models.Model):
    name = models.CharField(max_length=100)
    contact_data = models.CharField(max_length=100)
    experience = models.IntegerField()


class PerformerProfile(models.Model):
    name = models.CharField(max_length=100)
    contact_data = models.CharField(max_length=100)
    experience = models.IntegerField()

