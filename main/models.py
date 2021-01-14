from django.db import models

# Create your models here.


class Farmer(models.Model):
    farmer_id = models.AutoField
    name = models.CharField(max_length=100)
    mobile_no = models.IntegerField()
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    taluka = models.CharField(max_length=50)
    village = models.CharField(max_length=100)
    pincode = models.IntegerField()

    def __str__(self):
        return self.name


class Counselor(models.Model):
    counselor_id = models.AutoField
    name = models.CharField(max_length=100)
    mobile_no = models.IntegerField()
    address = models.CharField(max_length=300)
    education = models.CharField(max_length=200)

    def __str__(self):
        return self.name
