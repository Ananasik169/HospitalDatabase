from django import forms
from django.contrib.auth.forms import AuthenticationForm
from mainApp.models import User, Appointment


class UserLoginForm(AuthenticationForm):
    """Форма авторизации пользователя"""
    class Meta:
        model = User
        fields = ('username', 'password')


class AppointmentCreateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        exculde = 'date'
