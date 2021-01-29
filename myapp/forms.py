from django import forms
from .models import Student,signup, mypost

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        #fields=['fullname','email','sub','mobile']
        fields='__all__'

class SignupForm(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'

class MyPostForm(forms.ModelForm):
    class Meta:
        model=mypost
        fields='__all__'