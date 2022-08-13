from django import forms
from .models import User


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone']

    def __int__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)

        self.fields['username'].disabled = True




class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter your username '}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',  'placeholder': 'Enter your password'}))


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the valid email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your password'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Please confirm your password'}))



