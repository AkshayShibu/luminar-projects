from django import forms
from app.models import Students

# class Student_Form(forms.Form):
#     name=forms.CharField(max_length=50)
#     roll_no=forms.IntegerField()


# class Employee_Form(forms.Form):
#      name=forms.CharField(max_length=50)
#      emp_id=forms.IntegerField()
#      age=forms.IntegerField()
#      salary=forms.IntegerField()


class Student_Form(forms.ModelForm):
    class Meta:
        model=Students
        fields="__all__"