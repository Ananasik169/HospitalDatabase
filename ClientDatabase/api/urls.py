from django.contrib import admin
from django.urls import path, include
from api.views_auth_profile import LoginAPIView as auth_profile
from api.views import *

app_name = 'api'
urlpatterns = [
    path('appointment/create/', AppointmentCreateView.as_view()),
    path('all/', AppointmentListView.as_view()),
    path('users/login/', auth_profile.as_view()),
    # path('appointment/detail/<uuid:id>/', AppointmentDetailView.as_view()),
]
