from django import forms
from .models import studentinformation

class studentinformationform(forms.ModelForm):
    class Meta:
        model = studentinformation
        fields='__all__'