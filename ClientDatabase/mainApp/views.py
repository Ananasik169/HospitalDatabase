from django.contrib import auth
from django.contrib.auth import authenticate, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy


from .models import User, Appointment, Analyzes
from django.views import generic, View
from mainApp.forms import UserLoginForm, AppointmentCreateForm


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    num_patients = User.objects.filter(is_doctor__exact='False').all().count()
    num_appointments_all = Appointment.objects.count()
    # num_appointments_today = Appointment.objects.filter()

    return render(
        request,
        'index.html',
        context={'num_patients': num_patients, 'num_appointments_all': num_appointments_all},
    )


class DoctorListView(generic.ListView):
    model = User
    template_name = 'mainApp/doctor_list.html'


class UserDetailView(generic.DetailView):
    model = User


class AppointmentListView(generic.ListView):
    model = Appointment


class AppointmentDetailView(generic.DetailView):
    model = Appointment
    template_name = 'mainApp/appointment_detail.html'


class AppointmentCreateView(generic.CreateView):
    model = Appointment
    template_name = 'mainApp/appointment_create.html'
    success_url = reverse_lazy('mainApp:appointments')
    form_class = AppointmentCreateForm


class Login(LoginView):
    """Авторизация пользователя"""
    template_name = 'registration/login.html'
    authentication_form = UserLoginForm

    def post(self, request, *args, **kwargs):
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('mainApp:index'))
        # else:
        #     return HttpResponseRedirect(reverse('mainApp:login'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Программа контроля сроков документов'
        return context


class Logout(View):
    """Выход пользователя"""

    @staticmethod
    def get(request):
        logout(request)
        return HttpResponseRedirect(reverse('mainApp:index'))
