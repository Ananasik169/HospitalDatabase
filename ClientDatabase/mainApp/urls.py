from django.urls import path
from . import views


app_name = 'mainApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('doctors/', views.DoctorListView.as_view(), name='doctors'),
    path('doctors/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('appointment-create/', views.AppointmentCreateView.as_view(), name='appointment-create'),
    path('appointments/', views.AppointmentListView.as_view(), name='appointments'),
    path('appointments/<int:pk>', views.AppointmentDetailView.as_view(), name='appointment-detail'),
]
