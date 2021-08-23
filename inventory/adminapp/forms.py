from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
class Signform(UserCreationForm):
    class Meta:
        model=User
        fields='__all__'
        labels={'email:Email','username:Username','first_name:Firstname','last_name:Lastname','password1:Password','password2:confirmpassword'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Firstname'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Lastname'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email address'}),
            'password1': forms.PasswordInput(render_value=True, attrs={'class': 'form-control','placeholder': 'Password'}),
            'password2':  forms.PasswordInput(render_value=True, attrs={'class': 'form-control','placeholder': 'Confirm Password'}),
        }





class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))