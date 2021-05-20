from django.db import models


# Create your models here.
# coding: utf-8
class Tev(models.Model):
    id = models.AutoField(primary_key=True)
    equipment_number = models.CharField(max_length=255, blank=True, null=False)
    upload_time = models.DateTimeField(blank=True, null=False)
    max = models.FloatField(blank=True, null=False)
    average = models.FloatField(blank=True, null=False)
    pulse = models.FloatField(blank=True, null=False)
    electric = models.IntegerField(blank=True, null=False)

    class Meta:
        db_table = 'tev'


class Humiture(models.Model):
    id = models.AutoField(primary_key=True)
    equipment_number = models.CharField(max_length=255, blank=True, null=False)
    upload_time = models.DateTimeField(blank=True, null=False)
    temperature = models.IntegerField(blank=True, null=False)
    humidity = models.IntegerField(blank=True, null=False)

    class Meta:
        db_table = 'humiture'


class Picture(models.Model):
    id = models.AutoField(primary_key=True)
    image_name = models.CharField(max_length=255, blank=True, null=False)
    site = models.CharField(max_length=255, blank=True, null=False)
    path = models.CharField(max_length=255, blank=True, null=False)
    upload_time = models.DateTimeField(blank=True, null=False)

    class Meta:
        db_table = 'picture'
