from django import forms
from django.forms import ModelForm

from .models import FormModel

class StudentForm(forms.Form):
    student_name = forms.CharField(max_length=200)
    roll_number = forms.IntegerField()
    mobile_number=forms.CharField(max_length=200)
    date_of_birth=forms.DateTimeField()

class BookForm(ModelForm):
    class Meta:
            model = FormModel
            fields = fields = '__all__'


