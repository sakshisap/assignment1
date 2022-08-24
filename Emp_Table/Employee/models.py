from django.db import models

class Employee(models.Model): # define a model 
    Emp_name= models.CharField(max_length=20)
    Age= models.CharField(max_length=10)  
    Desg= models.CharField(max_length=20)
    
    def __str__(self):# this function is used to display name of instances for the model 
        
        return (self.Emp_name) 
    

# Create your models here.
