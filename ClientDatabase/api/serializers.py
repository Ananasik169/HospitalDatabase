from rest_framework import serializers
from mainApp.models import Appointment
from django.contrib.auth import authenticate
from mainApp.models import User


class AppointmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['user_id', 'doctor_id', 'complaint', 'date', 'status', 'pathologies', 'disease', 'prescription']


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'token']

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)
        if username is None:
            raise serializers.ValidationError(
                'Заполните поле логин'
            )
        if password is None:
            raise serializers.ValidationError(
                'Заполните поле пароль'
            )
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'Такого пользователя не существует.'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'Пользователь деактивирован'
            )

        return {'username': user.username,
                'token': user.token}
