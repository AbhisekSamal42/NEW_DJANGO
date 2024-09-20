from django.db import models

# Create your models here.
class Country(models.Model):
    Country_id=models.IntegerField(primary_key=True)
    Country_name=models.CharField(max_length=20)

    def __str__(self):
        return self.Country_id
    def __str__(self):
        return self.Country_name
class Capital(models.Model):
    Country_id=models.ForeignKey(Country,on_delete=models.CASCADE)
    Capial_id=models.IntegerField(primary_key=True)
    Capital_name=models.CharField(max_length=20)

    def __str__(self):
        return self.Capial_id
    def __str__(self):
        return self.Capital_name