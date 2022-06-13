from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.name


class InflectionTime(models.Model):
    data_field = models.DurationField()

    # def __str__(self):
    #     return self.data_field


class Component(models.Model):
    raw_component_url = models.FileField(upload_to='media', null=True)
    component_url = models.FileField(upload_to='media', null=True)
    business = models.ManyToManyField(Business)
    types = models.CharField(max_length=20)
    sub_type = models.CharField(max_length=30)
    # length = models.DurationField()

    inflection_time = models.ManyToManyField(InflectionTime)

    def __str__(self):
        return self.types


# Create your models here.
