from django import forms

class RegisterForm(forms.Form):
    Student_name = forms.CharField(max_length=100)
    Fathers_name = forms.CharField(max_length=100)
    mothers_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=10)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)