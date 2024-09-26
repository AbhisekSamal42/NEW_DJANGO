from django.db import models

# Create your models here.
class Country(models.Model):
    country_id=models.IntegerField(primary_key=True)
    country_name=models.CharField(max_length=30)

    def __str__(self):
        return self.country_id
    def __str__(self):
        return self.country_name
    
class Capital(models.Model):
    country_id=models.ForeignKey(Country,on_delete=models.CASCADE)
    capital_id=models.IntegerField(primary_key=True)
    capital_name=models.CharField(max_length=30)

    def __str__(self):
        return self.capital_id
    def __str__(self):
        return self.capital_name