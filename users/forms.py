from django import forms
from django.contrib.auth import password_validation
from .models import User


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class' : 'form-control' , 'placeholder':'Enter Password'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class' : 'form-control' , 'placeholder':'Confirm Password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'role',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }


class LoginForm(forms.Form):
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

    def clean_username(self):
        username = self.cleaned_data.get('username')

        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = None

        if user:
            return user.email
        return None


class PasswordChangeForm(forms.Form):
    """
    Form to change user password
    """
    current_password = forms.CharField(
        label='Current Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your current password'}),
        strip=False,
    )

    new_password = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your new password'}),
        strip=False,
    )

    confirm_new_password = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your new password password'}),
        strip=False,
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PasswordChangeForm, self).__init__(*args, **kwargs)

    def clean_current_password(self):
        current_password = self.cleaned_data["current_password"]
        if not self.user.check_password(current_password):
            raise forms.ValidationError('Incorrect current password')
        return current_password

    def clean_confirm_new_password(self):
        new_password = self.cleaned_data['new_password']
        confirm_new_password = self.cleaned_data['confirm_new_password']
        if new_password and confirm_new_password:
            if new_password != confirm_new_password:
                raise forms.ValidationError('Password mismatch')
        password_validation.validate_password(confirm_new_password, self.user)
        return confirm_new_password

    def save(self, commit=True):
        password = self.cleaned_data["confirm_new_password"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


class CreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'role',
        ]
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }