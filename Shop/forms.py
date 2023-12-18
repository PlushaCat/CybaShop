from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('phone', 'email', 'address')

        labels = {
            'phone': 'Номер телефона',
            'email': 'Email',
            'address': 'Адрес доставки',
        }

        widgets = {
            'phone': forms.TextInput(attrs={'class': 'colorMain mr-0.5'}),
            'email': forms.EmailInput(attrs={'class': 'colorMain mr-0.5'}),
            'address': forms.TextInput(attrs={'class': 'colorMain mr-0.5'}),
        }

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Ваше имя')


    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'email')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)