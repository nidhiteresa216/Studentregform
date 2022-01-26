from django import forms
from django.forms import ModelForm, fields
from .models import Details

#create a student form

class StudentForm(ModelForm):
    class Meta: 
        model = Details
        fields = ('first_name','last_name','birth_date','phone','email','address','college_name','course','about')
        labels= {
            'first_name': '',
            'last_name': '',
            'birth_date': '',
            'phone': '',
            'email': '',
            'address':'',
            'college_name': '',
            'course': '',
            'about':'',

        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'birth_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Date of Birth'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email ID'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'college_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'College Name'}),
            'course': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Course Name'}),
            'about': forms.TextInput(attrs={'class':'form-control', 'placeholder':'About'}),

        }
