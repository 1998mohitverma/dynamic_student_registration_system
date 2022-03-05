from django import forms
from .models import Student_Table

class Student_form(forms.ModelForm):
    class Meta:
        model = Student_Table
        fields = ['name','course','number','email']

        Labels = {
            'name':'Student Name',
            'course':'Course',
            'number':'University Registration Number',
            'email':'Email-Address'
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'course':forms.TextInput(attrs={'class':'form-control'}),
            'number':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }