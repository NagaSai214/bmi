from django.db import models


#BMI_Users is a model which is used to create table in MYSQL DB

class Bmi_Users( models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    height = models.FloatField(max_length=10)
    weight = models.FloatField(max_length=10)
    ph_no = models.CharField(max_length=30)
    bmi_index = models.FloatField(max_length=50)
    status = models.CharField(max_length=50)


# Meta is used to specify constraints for the table
    class Meta:
        managed: True
        db_table = 'Bmi_Users'
        unique_together = "ph_no",
