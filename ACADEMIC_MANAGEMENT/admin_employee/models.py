from django.db import models
from admin_general.models import*

# Create your models here.
class Employee_designation(models.Model):
    
    Emp_id=models.ForeignKey('Employee_registration',on_delete=models.CASCADE)
    Designation_id=models.ForeignKey(Designation,on_delete=models.CASCADE)
    From_date=models.DateField()
    To_date=models.DateField(blank=True,null=True)
    
class Employee_salary(models.Model):
    
    Emp_id=models.ForeignKey('Employee_registration',on_delete=models.CASCADE)
    Salary=models.DecimalField(max_digits=10, decimal_places=2)
    From_date=models.DateField()
    To_date=models.DateField(blank=True,null=True)
    
class Employee_department(models.Model):
    
    Emp_id=models.ForeignKey('Employee_registration',on_delete=models.CASCADE)
    Department_id=models.ForeignKey(Department,on_delete=models.CASCADE)
    From_date=models.DateField()
    To_date=models.DateField(blank=True,null=True)
    
    
    
    
    
    
class Employee_registration(models.Model):
    
    Employee_cat_id=models.ForeignKey(Emp_category,on_delete=models.CASCADE)
    Emp_name=models.CharField(max_length=255)
    Address=models.TextField()
    Dob=models.DateField()
    Email=models.EmailField()
    Mob=models.PositiveIntegerField()
    Qual_id=models.ForeignKey(Qualification,on_delete=models.CASCADE)
    Des_id=models.ForeignKey(Designation,on_delete=models.CASCADE)
    Dep_id=models.ForeignKey(Department,on_delete=models.CASCADE)
    Join_date=models.DateField()
    Salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Status = models.BooleanField(default=True)
    # Salary_date=models.DateField()
   
   
    # Salary_id=models.ForeignKey("Salary",on_delete=models.CASCADE)
    Photo=models.ImageField(upload_to='employee_photos/',blank=True,null=True)
    Barcode=models.ImageField(upload_to='barcode/',blank=True,null=True)

class CSD(models.Model):
    
    Emp_id=models.ForeignKey('Employee_registration',on_delete=models.CASCADE)
    Cls_id=models.ForeignKey(Master_class,on_delete=models.CASCADE)
    Div_id=models.ForeignKey(Division,on_delete=models.CASCADE)
    Sub_id=models.ForeignKey(Subject,on_delete=models.CASCADE)