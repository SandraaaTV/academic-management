from django.db import models

# Create your models here.
class Department(models.Model):
  Department_Name = models.CharField(max_length=255)
  Department_Code = models.CharField(max_length=50)
  Status = models.BooleanField(default=True)
  
class Designation(models.Model):
  Designation_Name = models.CharField(max_length=255)
  Designation_Code = models.CharField(max_length=255)
  Status = models.BooleanField(default=True)

class Qualification(models.Model):
  Qualification_Name = models.CharField(max_length=255)
  Status = models.BooleanField(default=True)
  
class Master_class(models.Model):
  Master_class_Name = models.CharField(max_length=255)
  Status = models.BooleanField(default=True)
  
class Division(models.Model):
  Division_Name = models.CharField(max_length=255)
  Status = models.BooleanField(default=True)

class Emp_category(models.Model):
  
  EMPLOYEE_CATEGORY_CHOICES=[
    (1,'Accountant'),
    (2,'Cafeteria'),
    (3,'Librarian'),
    (4,'Teacher'),
    (5,'Other'),
  
    
  ]
  Employee_Name = models.CharField(max_length=255)
  Employee_Area = models.IntegerField(choices=EMPLOYEE_CATEGORY_CHOICES)
  Status = models.BooleanField(default=True)
  
  
class Subject(models.Model):
  Subject_Name = models.CharField(max_length=100)
  Status = models.BooleanField(default=True)
  
class SubjectClass(models.Model):
  Subject_Id = models.ForeignKey("Subject",on_delete=models.CASCADE)
  Class_Id = models.ForeignKey("Master_class",on_delete=models.CASCADE)
  
  
  
