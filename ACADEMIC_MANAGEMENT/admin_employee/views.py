from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.template import loader
from admin_general.models import *
from admin_employee.models import *
from django.conf import settings
# Create your views here.
def employee_register(request):
    qualification_data=Qualification.objects.filter(Status=True)
    designation_data=Designation.objects.filter(Status=True)
    department_data=Department.objects.filter(Status=True)
    employee_data=Emp_category.objects.filter(Status=True)
    class_data=Master_class.objects.filter(Status=True)
    division_data=Division.objects.filter(Status=True)
    subject_data=Subject.objects.filter(Status=True)
    
    context={
        'qualification_data':qualification_data, 
        'designation_data':designation_data,
        'department_data':department_data,
        'employee_data':employee_data,
        'class_data':class_data,
        'division_data':division_data,
        'subject_data':subject_data,
        

    }
    
    
    return render(request,"employee_register.html",context)
def get_subjects_by_class(request):
    class_id = request.GET.get('class_id', None)
    subjects = SubjectClass.objects.filter(Class_Id=class_id).values('Subject_Id__id', 'Subject_Id__Subject_Name')

    return JsonResponse(list(subjects), safe=False)



def employee_add(request):
  template = loader.get_template('employee_add.html')
  return HttpResponse(template.render())


