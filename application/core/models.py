from django.db import models

# Create your models here.

class  Patient(models.Model):
	first_name = models.CharField(max_length=80)
	last_name = models.CharField(max_length=80)
	age_firstentry = models.IntegerField(default = 0)
	gender = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('US', 'Unspecified'),
    
		]