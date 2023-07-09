from django.db import models

class Bmi_Users( models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    height = models.FloatField(max_length=10)
    weight = models.FloatField(max_length=10)
    ph_no = models.CharField(max_length=30)
    bmi_index = models.FloatField(max_length=50)
    status = models.CharField(max_length=50)


    class Meta:
        managed: True
        db_table = 'Bmi_Users'
        unique_together = "ph_no",
