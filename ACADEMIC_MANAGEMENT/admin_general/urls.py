from django.urls import path
from . import views
urlpatterns = [
    
    path('base/', views.base,name='base'),
    
    path('admin_master_dep/', views.admin_master_dep,name='admin_master_department'),
    path('department_edit/', views.department_edit,name='department_edit'),
    path('department_update/', views.department_update,name='department_update'),
    path('department_delete/', views.department_delete,name='department_delete'),
    
    path('admin_master_des/', views.admin_master_des,name='admin_master_designation'), 
    path('designation_edit/', views.designation_edit,name='designation_edit'),
    path('designation_update/', views.designation_update,name='designation_update'),
    path('designation_delete/', views.designation_delete,name='designation_delete'),
    
    path('admin_master_qua/', views.admin_master_qua,name='admin_master_qualification'),
    path('qualification_edit/', views.qualification_edit,name='qualification_edit'),
    path('qualification_update/', views.qualification_update,name='qualification_update'),
    path('qualification_delete/', views.qualification_delete,name='qualification_delete'),
    
    path('admin_master_class/', views.admin_master_class,name='admin_master_class'),
    path('class_edit/', views.class_edit,name='class_edit'),
    path('class_update/', views.class_update,name='class_update'),
    path('class_delete/', views.class_delete,name='class_delete'),
    
    path('admin_master_division/', views.admin_master_division,name='admin_master_division'),
    path('division_edit/', views.division_edit,name='division_edit'),
    path('division_update/', views.division_update,name='division_update'),
    path('division_delete/', views.division_delete,name='division_delete'),
    
    path('admin_master_emp_category/', views.admin_master_emp_category,name='admin_master_emp_category'),
    path('employee_edit/', views.employee_edit,name='employee_edit'),
    path('employee_update/', views.employee_update,name='employee_update'),
    path('employee_delete/', views.employee_delete,name='employee_delete'),
   
   
    path('admin_master_subject/', views.admin_master_subject,name='admin_master_subject'),
    path('subject_edit/', views.subject_edit,name='subject_edit'),
    path('subject_update/', views.subject_update,name='subject_update'),
    path('subject_delete/', views.subject_delete,name='subject_delete'),
   
    

    
   

]