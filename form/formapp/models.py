from django.db import models
#
# Create your models here.
class FormModel(models.Model):
    student_name=models.CharField(max_length=200)
    roll_number=models.CharField(max_length=200)
#     mobile_number=models.CharField(max_length=200)
#     date_of_birth=models.DateTimeField()
#
def __str__(self):
    return "student_name={0},roll_number={1}".format(self.student_name,self.roll_number)