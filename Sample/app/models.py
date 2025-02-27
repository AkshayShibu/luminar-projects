from django.db import models

# Create your models here.

class Students(models.Model):
    name=models.CharField(max_length=50)
    roll_no=models.PositiveIntegerField()


# class Employee(models.Model):
#     name=models.CharField(max_length=50)
#     emp_id=models.PositiveIntegerField()
#     age=models.PositiveIntegerField()
#     salary=models.PositiveIntegerField()
    