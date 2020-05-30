from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

class Device(models.Model):
    uid = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{self.uid} {self.name}'.format(self=self)

class TemperatureReading(models.Model):
    device = models.ForeignKey('Device',to_field='uid',on_delete=models.CASCADE)
    reading = models.IntegerField(validators=[MinValueValidator(-50), MaxValueValidator(100)])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{self.device} - {self.reading} - {self.date}'.format(self=self)

class HumidityReading(models.Model):
    device = models.ForeignKey('Device',to_field='uid',on_delete=models.CASCADE)
    reading = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{self.device} - {self.reading} - {self.date}'.format(self=self)