from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.template import loader
from .models import *
from django.conf import settings
# Create your views here.



def base(request):
  
  template = loader.get_template('base.html')
  return HttpResponse(template.render())
   
# ADMIN_MASTER_DEPARTMENT_STARTING
def admin_master_dep(request):
      error=""
      success=""
      
      if request.method == 'POST':
        department_name = request.POST.get('department_name').strip()
        department_code = request.POST.get('department_code').strip()

        # Validation checks
        if not department_name or not department_code:
          # Handle missing data error
            error="both fields are required"
            
        elif Department.objects.filter(Department_Name=department_name,Department_Code=department_code).exists():
          # Handle duplicate department name error
            error="Department Name and code are already exist"
                
        elif Department.objects.filter(Department_Name=department_name).exists():
          # Handle duplicate department name error
            error="Department Name already exist"
            
        elif Department.objects.filter(Department_Code=department_code).exists(): 
          # Handle duplicate department code error
            error="DEpartment Code already exist"
            
        # Save the data to the database
        else :
          department = Department(Department_Name=department_name, Department_Code=department_code)
          department.save()
          success="submitted"
          
      departments = Department.objects.all()
      return render(request, 'admin_master_department.html', {'departments': departments,'error_msg':error,'success_msg':success})

def department_edit(request):
  id_var=request.GET['id'] #db id
  response_data= Department.objects.get(id=id_var) 
  serialized_data={
    'name': response_data.Department_Name,
    'code': response_data.Department_Code,
    'status':1 if response_data.Status else 0,
  }
  return JsonResponse(serialized_data)

def department_update(request):
  # ///
  error=""
  success=""
  
  id=request.GET['id']
  name=request.GET['name']
  code=request.GET['code']
  status=request.GET['status']

  
  if not name or not code:
      error="both fields are required"
      
  elif Department.objects.filter(Department_Name=name,Department_Code=code).exclude(id=id).exists():
      error="Department Name and code are already exist" 
      
  elif Department.objects.filter(Department_Name=name).exclude(id=id).exists():
          # Handle duplicate department name error
      error="Department Name already exist"
            
  elif Department.objects.filter(Department_Code=code).exclude(id=id).exists(): 
          # Handle duplicate department code error
      error="Department Code already exist"
            
        # Save the data to the database
  else :
      department = Department.objects.get(id=id)
      department.Department_Name=name
      department.Department_Code=code
      department.Status=status
      department.save()
      success="updated successfully"
      

          
    
  return JsonResponse({'error_msg':error,'success_msg':success})


def department_delete(request):
   dlt_id=request.GET.get('id')
   try:
      department = Department.objects.get(id=dlt_id)
      department.delete()
      return JsonResponse({'success':'Department deleted successfully'})
   except Department.DoesNotExist:
      return JsonResponse({'error':'Department not found'}, status=404) 

  
# ADMIN_MASTER_DEPARTMENT_ENDING
# ADMIN_MASTER_DESIGNATION_STARTING

def admin_master_des(request):
      error=""
      success=""
      
      if request.method == 'POST':
        designation_name = request.POST.get('designation_name').strip()
        designation_code = request.POST.get('designation_code').strip()

        # Validation checks
        if not designation_name or not designation_code:
          # Handle missing data error
            error="both fields are required"
            
        elif Designation.objects.filter(Designation_Name=designation_name,Designation_Code=designation_code).exists():
          # Handle duplicate department name error
            error="Designation Name and code are already exist"
                
        elif Designation.objects.filter(Designation_Name=designation_name).exists():
          # Handle duplicate department name error
            error="Designation Name already exist"
            
        elif Designation.objects.filter(Designation_Code=designation_code).exists(): 
          # Handle duplicate department code error
            error="Designation Code already exist"
            
            
                    # Save the data to the database
        else :
          department = Designation(Designation_Name=designation_name, Designation_Code=designation_code)
          department.save()
          success="submitted"
          
      designations = Designation.objects.all()
      return render(request, 'admin_master_designation.html', {'designations': designations,'error_msg':error,'success_msg':success})

def designation_edit(request):
  id_var=request.GET['id'] #db id
  response_data= Designation.objects.get(id=id_var) 
  serialized_data={
    'name': response_data.Designation_Name,
    'code': response_data.Designation_Code,
    'status':1 if response_data.Status else 0,
  }
  return JsonResponse(serialized_data)

def designation_update(request):
  # ///
  error=""
  success=""
  
  id=request.GET['id']
  name=request.GET['name']
  code=request.GET['code']
  status=request.GET['status']

  
  if not name or not code:
      error="both fields are required"
      
  elif Designation.objects.filter(Designation_Name=name,Designation_Code=code).exclude(id=id).exists():
      error="Designation Name and code are already exist" 
      
  elif Designation.objects.filter(Designation_Name=name).exclude(id=id).exists():
          # Handle duplicate department name error
      error="Designation Name already exist"
            
  elif Designation.objects.filter(Designation_Code=code).exclude(id=id).exists(): 
          # Handle duplicate department code error
      error="Designation Code already exist"
            
        # Save the data to the database
  else :
      designation = Designation.objects.get(id=id)
      designation.Designation_Name=name
      designation.Designation_Code=code
      designation.Status=status
      designation.save()
      success="updated successfully"
      

          
    
  return JsonResponse({'error_msg':error,'success_msg':success})


def designation_delete(request):
   dlt_id=request.GET.get('id')
   try:
      designation = Designation.objects.get(id=dlt_id)
      designation.delete()
      return JsonResponse({'success':'Designation deleted successfully'})
   except Designation.DoesNotExist:
      return JsonResponse({'error':'Designation not found'}, status=404) 

    
  # ADMIN_MASTER_DESIGNATION_ENDING
  # ADMIN_MASTER_QUALIFICATION_STARTING

def admin_master_qua(request):
      error=""
      success=""
      
      if request.method == 'POST':
        qualification_name = request.POST.get('qualification_name').strip()
        
        # Validation checks
        if not qualification_name :
          # Handle missing data error
            error="both fields are required"
                
        elif Qualification.objects.filter(Qualification_Name=qualification_name).exists():
          # Handle duplicate department name error
            error="Department Name already exist"
            
                    # Save the data to the database
        else :
          qualification = Qualification(Qualification_Name=qualification_name)
          qualification.save()
          success="submitted"
          
      qualifications = Qualification.objects.all()
      return render(request, 'admin_master_qualification.html', {'qualifications': qualifications,'qua_error_msg':error,'qua_success_msg':success})

def qualification_edit(request):
  id_var=request.GET['id'] #db id
  response_data= Qualification.objects.get(id=id_var) 
  serialized_data={
    'name': response_data.Qualification_Name,
    'status':1 if response_data.Status else 0,
  }
  return JsonResponse(serialized_data)

def qualification_update(request):
  # ///
  error=""
  success=""
  
  id=request.GET['id']
  name=request.GET['name']
  status=request.GET['status']

  
  if not name :
      error="Name field required"
      
 
      
  elif Qualification.objects.filter(Qualification_Name=name).exclude(id=id).exists():
          # Handle duplicate department name error
      error="Department Name already exist"
            
 
            
        # Save the data to the database
  else :
      qualification = Qualification.objects.get(id=id)
      qualification.Qualification_Name=name
      qualification.Status=status
      qualification.save()
      success="updated successfully"
      

          
    
  return JsonResponse({'error_msg':error,'success_msg':success})


def qualification_delete(request):
   dlt_id=request.GET.get('id')
   try:
      qualification = Qualification.objects.get(id=dlt_id)
      qualification.delete()
      return JsonResponse({'success':'qualification deleted successfully'})
   except Qualification.DoesNotExist:
      return JsonResponse({'error':'qualification not found'}, status=404) 

  

  # ADMIN_MASTER_QUALIFICATION_ENDING
  # ADMIN_MASTER_CLASS_STARTING
  
def admin_master_class(request):
      error=""
      success=""
      
      if request.method == 'POST':
        class_name = request.POST.get('class_name').strip()
        
        # Validation checks
        if not class_name :
          # Handle missing data error
            error="both fields are required"
                
        elif Master_class.objects.filter(Master_class_Name=class_name).exists():
          # Handle duplicate department name error
            error="Department Name already exist"
            
                    # Save the data to the database
        else :
          master_class = Master_class(Master_class_Name=class_name)
          master_class.save()
          success="submitted"
          
      master_classes = Master_class.objects.all()
      return render(request, 'admin_master_class.html', {'master_classes': master_classes,'cls_error_msg':error,'cls_success_msg':success})

def class_edit(request):
  id_var=request.GET['id'] #db id
  response_data= Master_class.objects.get(id=id_var) 
  serialized_data={
    'name': response_data.Master_class_Name,
    'status':1 if response_data.Status else 0,
  }
  return JsonResponse(serialized_data)

def class_update(request):
  # ///
  error=""
  success=""
  
  id=request.GET['id']
  name=request.GET['name']
  status=request.GET['status']

  
  if not name :
      error="Name field required"
      
 
      
  elif Master_class.objects.filter(Master_class_Name=name).exclude(id=id).exists():
          # Handle duplicate department name error
      error="Class Name already exist"
            
 
            
        # Save the data to the database
  else :
      master_class = Master_class.objects.get(id=id)
      master_class.Master_class_Name=name
      master_class.Status=status
      master_class.save()
      success="updated successfully"
      

          
    
  return JsonResponse({'error_msg':error,'success_msg':success})


def class_delete(request):
   dlt_id=request.GET.get('id')
   try:
      master_class = Master_class.objects.get(id=dlt_id)
      master_class.delete()
      return JsonResponse({'success':'class deleted successfully'})
   except Master_class.DoesNotExist:
      return JsonResponse({'error':'class not found'}, status=404) 

  

# ADMIN_MASTER_CLASS_ENDING
# ADMIN_MASTER_DIVISION_STARTING
  
def admin_master_division(request):
      error=""
      success=""
      
      if request.method == 'POST':
        division_name = request.POST.get('division_name').strip()
        
        # Validation checks
        if not division_name :
          # Handle missing data error
            error="both fields are required"
                
        elif Division.objects.filter(Division_Name=division_name).exists():
          # Handle duplicate department name error
            error="Department Name already exist"
            
                    # Save the data to the database
        else :
          division = Division(Division_Name=division_name)
          division.save()
          success="submitted"
          
      divisions = Division.objects.all()
      return render(request, 'admin_master_division.html', {'divisions': divisions,'div_error_msg':error,'div_success_msg':success})

def division_edit(request):
  id_var=request.GET['id'] #db id
  response_data= Division.objects.get(id=id_var) 
  serialized_data={
    'name': response_data.Division_Name,
    'status':1 if response_data.Status else 0,
  }
  return JsonResponse(serialized_data)

def division_update(request):
  # ///
  error=""
  success=""
  
  id=request.GET['id']
  name=request.GET['name']
  status=request.GET['status']

  
  if not name :
      error="Name field required"
      
 
      
  elif Division.objects.filter(Division_Name=name).exclude(id=id).exists():
          # Handle duplicate department name error
      error="Department Name already exist"
            
 
            
        # Save the data to the database
  else :
      division = Division.objects.get(id=id)
      division.Division_Name=name
      division.Status=status
      division.save()
      success="updated successfully"
      

          
    
  return JsonResponse({'error_msg':error,'success_msg':success})


def division_delete(request):
   dlt_id=request.GET.get('id')
   try:
      division = Division.objects.get(id=dlt_id)
      division.delete()
      return JsonResponse({'success':'qualification deleted successfully'})
   except Division.DoesNotExist:
      return JsonResponse({'error':'qualification not found'}, status=404) 

# ADMIN_MASTER_DIVISION_ENDING


 
# def admin_master_emp_category(request):
#   return render(request,'admin_master_emp_category.html')
  
# employee
 
def admin_master_emp_category(request):
    error=""
    success=""
      
    if request.method == 'POST':
       employee_name = request.POST.get('employee_name').strip()
       employee_area = request.POST.get('employee_area').strip()

        # Validation checks
       if not employee_name or not employee_area:
          # Handle missing data error
            error="both fields are required"
            
      #  elif Emp_category.objects.filter(Employee_Name=employee_name,Employee_Area=employee_area).exists():
      #     # Handle duplicate department name error
      #       error="Emp_category Name and area are already exist"
                
       elif Emp_category.objects.filter(Employee_Name=employee_name).exists():
          # Handle duplicate department name error
            error="Emp_category Name already exist"
            
      #  elif Emp_category.objects.filter(Employee_Area=employee_area).exists(): 
      #     # Handle duplicate department code error
      #       error="Emp_category area already exist"
            
        # Save the data to the database
       else :
          employee = Emp_category(Employee_Name=employee_name, Employee_Area=employee_area)
          employee.save()
          success="submitted"
          
    employees = Emp_category.objects.all()
    return render(request, 'admin_master_emp_category.html',{'settings': settings,'employees':employees,'error_msg':error,'success_msg':success})

  # return render(request,'admin_master_emp_category.html',{'settings': settings})

def employee_edit(request):
  id_var=request.GET['id'] #db id
  response_data= Emp_category.objects.get(id=id_var) 
  serialized_data={
    'name': response_data.Employee_Name,
    'area': response_data.Employee_Area,
    'status':1 if response_data.Status else 0,
  }
  return JsonResponse(serialized_data)

def employee_update(request):
  # ///
  error=""
  success=""
  
  id=request.GET['id']
  name=request.GET['name']
  area=request.GET['area']
  status=request.GET['status']

  
  if not name or not area:
      error="both fields are required"
      
  # elif Emp_category.objects.filter(Employee_Name=name,Employee_Area=area).exclude(id=id).exists():
  #     error="Employee Name and area are already exist" 
      
  elif Emp_category.objects.filter(Employee_Name=name).exclude(id=id).exists():
          # Handle duplicate department name error
      error="Employee Name already exist"
            
  # elif Emp_category.objects.filter(Employee_Area=area).exclude(id=id).exists(): 
  #         # Handle duplicate department code error
  #     error="Employee area already exist"
            
        # Save the data to the database
  else :
      employee = Emp_category.objects.get(id=id)
      employee.Employee_Name=name
      employee.Employee_Area=area
      employee.Status=status
      employee.save()
      success="updated successfully"
      

          
    
  return JsonResponse({'error_msg':error,'success_msg':success})


def employee_delete(request):
   dlt_id=request.GET.get('id')
   try:
      employee =Emp_category.objects.get(id=dlt_id)
      employee.delete()
      return JsonResponse({'success':'employee deleted successfully'})
   except employee.DoesNotExist:
      return JsonResponse({'error':'employee not found'}, status=404) 
    
# def admin_master_subject(request):
#   all=Master_class.objects.filter(Status=1)
#   return render(request,'admin_master_subject.html',{'list':all})

# ADMIN_MASTER_STUDENT_STARTING
def admin_master_subject(request):
      error=""
      success=""
      
      if request.method == 'POST':
        subject_name = request.POST.get('subject_name').strip()
        
        # Validation checks
        if not subject_name :
          # Handle missing data error
            error="subject_name field is required"
                
        elif Subject.objects.filter(Subject_Name=subject_name).exists():
          # Handle duplicate department name error
            error="Department Name already exist"
            
                    # Save the data to the database
        else :
          
          chkvalue=request.POST.getlist('check_id')
          if chkvalue:
            subject_obj,create=Subject.objects.get_or_create(Subject_Name=subject_name)
            for chkid in chkvalue:
              clasins=get_object_or_404(Master_class,pk=int(chkid))
              objins=SubjectClass(Subject_Id=subject_obj,Class_Id=clasins)
              objins.save()
            success="submitted"
      all=Master_class.objects.filter(Status=1)   
      subjects = Subject.objects.all()
      return render(request, 'admin_master_subject.html', {'list':all, 'subjects': subjects,'sub_error_msg':error,'sub_success_msg':success})




def subject_edit(request):
  id_var=request.GET['id'] #db id
  response_data= Subject.objects.get(id=id_var) 
  class_data=SubjectClass.objects.filter(Subject_Id=id_var).values_list('Class_Id__Master_class_Name',flat=True)
  serialized_data={
    'name': response_data.Subject_Name,
    'status':1 if response_data.Status else 0,
    'class_details':list(class_data)
    
  }
  return JsonResponse(serialized_data)

def subject_update(request):
  # ///
  error=""
  success=""
  
  id=request.GET['id']
  name=request.GET['name']
  status=request.GET['status']

  
  if not name :
      error="Name field required"
      
 
      
  elif Subject.objects.filter(Subject_Name=name).exclude(id=id).exists():
          # Handle duplicate department name error
      error="Department Name already exist"
            
 
            
        # Save the data to the database
  else :
      subject = Subject.objects.get(id=id)
      subject.Subject_Name=name
      subject.Status=status
      subject.save()
      success="updated successfully"
      

          
    
  return JsonResponse({'error_msg':error,'success_msg':success})


def subject_delete(request):
   dlt_id=request.GET.get('id')
   try:
      subject = Subject.objects.get(id=dlt_id)
      subject.delete()
      return JsonResponse({'success':'Subject deleted successfully'})
   except Subject.DoesNotExist:
      return JsonResponse({'error':'Subject not found'}, status=404) 

  

# ADMIN_MASTER_STUDENT_ENDING