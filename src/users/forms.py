from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, AbstractBaseUser

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class' : 'form-control' , 'placeholder':'Enter Password'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class' : 'form-control' , 'placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
        }


class LoginForm(AuthenticationForm):
    """
        Form to login a user
        """
    username = forms.CharField(
        label='username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        strip=False,
    )
