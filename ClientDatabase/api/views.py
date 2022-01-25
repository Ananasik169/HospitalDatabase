from django.shortcuts import render
from rest_framework import generics
from api.serializers import AppointmentDetailSerializer, AppointmentListSerializer
from mainApp.models import Appointment
from api.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentDetailSerializer


class AppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentListSerializer
    queryset = Appointment.objects.all()
    permission_classes = (IsAuthenticated,)


# class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = AppointmentDetailSerializer
#     queryset = Appointment.objects.all()
#     permission_classes = (IsOwnerOrReadOnly, IsAdminUser,)
