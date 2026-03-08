from django.urls import path
from . import views


urlpatterns = [

    path('patients', views.register_patient),

    path('reports', views.upload_report),

    path('patients/<int:id>/reports', views.patient_reports),

]