from django.db import models

# Create your models here.
class Business(models.Model):
    series_reference=models.CharField(max_length=100)
    period=models.FloatField()
    Data_value=models.CharField(max_length=100)
    Suppressed=models.CharField(max_length=100,null=True)
    STATUS=models.CharField(max_length=100)
    UNITS=models.CharField(max_length=100)
    Magnitude=models.IntegerField()
    Subject=models.CharField(max_length=100)
    Group=models.CharField(max_length=100)
    Series_title_1=models.CharField(max_length=100)
    def __str__(self):
        return self.series_reference