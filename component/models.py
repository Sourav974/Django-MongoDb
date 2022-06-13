from django.db import models

# Create your models here.


class BusinessComponent1(models.Model):
    name = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.name


class InflectionTimeComponent1(models.Model):
    data_field = models.DecimalField(max_digits=5, decimal_places=2)


# Create your models here.
class TextBox(models.Model):
    position_x = models.CharField(max_length=10)
    position_y = models.CharField(max_length=10)
    height = models.IntegerField()
    width = models.IntegerField()
    start_time = models.DecimalField(max_digits=5, decimal_places=2)
    end_time = models.DecimalField(max_digits=5, decimal_places=2)
    opacity = models.IntegerField()

    def __str__(self):
        return self.position_x


class LogoSlot(models.Model):
    position_x = models.CharField(max_length=10)
    position_y = models.CharField(max_length=10)
    height = models.IntegerField()
    width = models.IntegerField()
    start_time = models.DecimalField(max_digits=5, decimal_places=2)
    end_time = models.DecimalField(max_digits=5, decimal_places=2)
    opacity = models.IntegerField()

    def __str__(self):
        return self.position_y


class Component1(models.Model):
    component_url = models.FileField(upload_to='media', null=True)
    types = models.CharField(max_length=20)
    sub_type = models.CharField(max_length=30)
    length = models.DecimalField(max_digits=5, decimal_places=2, default=None)
    business = models.ManyToManyField(BusinessComponent1)
    inflection_time = models.ManyToManyField(InflectionTimeComponent1)
    text_box = models.ForeignKey(TextBox, on_delete=models.CASCADE)
    logo_slot = models.ForeignKey(LogoSlot, on_delete=models.CASCADE)

    def __str__(self):
        return self.types
