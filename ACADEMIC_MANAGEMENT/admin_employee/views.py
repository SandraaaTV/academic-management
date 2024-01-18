from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.template import loader
from admin_general.models import *
from admin_employee.models import *
from django.conf import settings
import qrcode
from django.core.files.base import ContentFile
from io import BytesIO


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
    
    
    if request.POST:
      a=request.POST['category']
      emparray=a.split('_')
      emp_id =Emp_category.objects.get(id=emparray[0])
  
      name=request.POST['name']
      address=request.POST['address']
      dob=request.POST['dob']
      # d=request.POST['Gender']
      email=request.POST['email']
      # f=request.POST['countryCode']
      phone=request.POST['phone']
      g=request.POST['qualification']
      q_id=Qualification.objects.get(id=g)
      h=request.POST['designation']
      des_id=Designation.objects.get(id=h)
      i=request.POST['department']
      dep_id=Department.objects.get(id=i)
      
      
      
     
      # # j=request.POST['d_status']
      # did=Designation.objects.get(id=j)
      date_of_join=request.POST['Date_Of_Joining']
      salary=request.POST['salary']
      
      qr_content = f"{name} | {date_of_join} | {dep_id}"

        # Create a QR code instance
      qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Add data to the QR code
      qr.add_data(qr_content)
      qr.make(fit=True)

        # Create an image from the QR code
      img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a BytesIO object
      img_bytes = BytesIO()
      img.save(img_bytes)
      
      # m=request.POST['Salary Date']
      n=request.FILES['file']
      employee_detail=Employee_registration(
        Employee_cat_id=emp_id,
        Emp_name=name, 
        Address=address,
        Dob=dob,
        Email=email, 
        Mob=phone,
        Qual_id=q_id,
        Des_id=des_id,
        Dep_id=dep_id,
        Join_date=date_of_join,
        Salary=salary,
        Photo=n)
      employee_detail.Barcode.save(f"{name}_barcode.png", ContentFile(img_bytes.getvalue()), save=False)
      employee_detail.save()
      empid = employee_detail.id
      empidins=Employee_registration.objects.get(id=empid)
      
      #employee department
      obj = Employee_department(Emp_id=empidins, Department_id=dep_id, From_date=date_of_join)
      obj.save()
      
      
      # Create Employee_designation
        # Create Employee_designation
      emp_desig = Employee_designation(Emp_id=empidins, Designation_id=des_id, From_date=date_of_join)
      emp_desig.save()

        # Create Employee_salary
      # Create Employee_salary
      emp_salary = Employee_salary(Emp_id=empidins, Salary=salary, From_date=date_of_join)
      emp_salary.save()


      class_id = request.POST.getlist('classId')
      div_id = request.POST.getlist('divisionId')
      sub_id = request.POST.getlist('subjectId')
      print(class_id, div_id, sub_id)

      if class_id:
          for classid, sub, div in zip(class_id, div_id, sub_id):
              cls_instance = get_object_or_404(Master_class, pk=int(classid))
              sub_instance = get_object_or_404(Subject, pk=int(sub))
              div_instance = get_object_or_404(Division, pk=int(div))

              obj = CSD(Emp_id=empidins, Cls_id=cls_instance, Sub_id=sub_instance, Div_id=div_instance)
              obj.save()
      # Create CSD
        
      
    return render(request,"employee_register.html",context)
  
  
  
  
  
  
  
def get_subjects_by_class(request):
    class_id = request.GET.get('class_id', None)
    subjects = SubjectClass.objects.filter(Class_Id=class_id).values('Subject_Id__id', 'Subject_Id__Subject_Name')

    return JsonResponse(list(subjects), safe=False)



# def employee_add(request):
#   template = loader.get_template('employee_add.html')
#   return HttpResponse(template.render())


def employee_add(request):
  template = loader.get_template('employee_add.html')
  d=Employee_registration.objects.all()
  return HttpResponse(template.render({"employee":d}))
