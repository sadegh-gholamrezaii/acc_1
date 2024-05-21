from django import forms


class UserRegisterationForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32, min_length=8) 
    phone_number = forms.DecimalField(max_digits=11, decimal_places=0)
    email = forms.EmailField()


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32, min_length=8)