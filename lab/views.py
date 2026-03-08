from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from .utils import *

# Create your views here.


# Register Patient 
@api_view(['POST'])
def register_patient(request):

    serializer = PatientSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Upload Lab Report
@api_view(['POST'])
def upload_report(request):

    serializer = LabReportSerializer(data=request.data)

    if serializer.is_valid():
        report = serializer.save()

        patient = report.patient
        report_link = report.report_file.url

        send_report_sms(patient.phone, report_link)

        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Fetch Patient Reports
@api_view(['GET'])
def patient_reports(request, id):

    reports = LabReport.objects.filter(patient_id=id)

    serializer = LabReportSerializer(reports, many=True)

    return Response(serializer.data)

