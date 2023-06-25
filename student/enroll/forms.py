from django import forms
from .models import *

class studentForm(forms.ModelForm):
    class Meta:
        model=StudentInfo
        fields='__all__'
    
