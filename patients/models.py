from django.db import models
GENDER = (("Male", "Male"), ("Female", "Female"))


# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    anaemia = models.BooleanField(default=False)
    ejection_fraction = models.FloatField()
    creatinine_phosphokinase = models.FloatField()
    diabetes = models.BooleanField(default=False)
    high_blood_pressure = models.BooleanField(default=False)
    platelets = models.FloatField()
    serum_creatinine = models.FloatField()
    serum_sodium = models.FloatField()
    sex = models.CharField(max_length=20, choices=GENDER)
    smoking = models.BooleanField(default=False)
    time = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.age} years"
