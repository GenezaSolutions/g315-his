from django.db import models

# Create your models here.

class  Patient(models.Model):
	first_name = models.CharField(max_length=80)
	last_name = models.CharField(max_length=80)
	birth_date = models.DateField()
	gender = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('US', 'Unspecified'),
		]
	father_name = models.CharField(max_length=80)
	state = models.CharField(max_length=80)
	district = models.CharField(max_length=40)
	mobile = models.IntegerField()
	ID_number = models.IntegerField()
	ID_type = models.CharField(max_length=40)
	city = models.CharField(max_length=40)
	pincode = models.CharField(max_length=6)
	village = models.CharField(max_length=40)
	
	


