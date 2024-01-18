from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('employee_register/', views.employee_register, name='employee_register'),
    path('employee_add/', views.employee_add, name='employee_add'),
    path('get_subjects_by_class/', views.get_subjects_by_class, name='get_subjects_by_class'),
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)