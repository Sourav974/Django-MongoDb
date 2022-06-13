from django.db import models
# from template.models import *
# Create your models here.


class SuperBackgroundScore(models.Model):
    score_url = models.FileField(upload_to='media', null=True)
    start_time = models.FloatField()
    end_time = models.FloatField()


class SuperComponents(models.Model):
    slot_id = models.IntegerField()
    component_url = models.FileField(upload_to='media', null=True)
    types = models.CharField(max_length=50)
    start_time = models.DecimalField(max_digits=5, decimal_places=2)
    end_time = models.DecimalField(max_digits=5, decimal_places=2)


class SuperTextElement(models.Model):
    text = models.CharField(max_length=100)
    font = models.CharField(max_length=30)
    font_size = models.CharField(max_length=10)
    position_x = models.CharField(max_length=10)
    position_y = models.CharField(max_length=10)
    start_time = models.FloatField()
    end_time = models.FloatField()

    def __str__(self):
        return self.font


class SuperLogos(models.Model):
    logo_url = models.FileField(upload_to='media', null=True)
    start_time = models.FloatField()
    end_time = models.FloatField()
    transition_in = models.CharField(max_length=20)
    transition_out = models.CharField(max_length=20)


class SuperOverlays(models.Model):
    text_element = models.ManyToManyField(SuperTextElement)
    logos = models.ManyToManyField(SuperLogos)


class SuperTemplate(models.Model):
    business = models.CharField(max_length=50)
    types = models.CharField(max_length=30)
    duration = models.DurationField()
    template_url = models.FileField(upload_to='media', null=True)
    background_score = models.ForeignKey(
        SuperBackgroundScore, on_delete=models.CASCADE)
    components = models.ManyToManyField(SuperComponents)
    overlays = models.ForeignKey(SuperOverlays, on_delete=models.CASCADE)
