from django.db import models

# Create your models here.

class Patient(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)

class LabReport(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    report_name = models.CharField(max_length=200)
    report_file = models.FileField(upload_to="reports/")
    uploaded_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.report_name