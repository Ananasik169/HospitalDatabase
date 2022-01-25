from django.db import models
import jwt
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# from django.urls import reverse
import uuid
from ClientDatabase.settings import SECRET_KEY

from django.urls import reverse


class User(AbstractUser):
    """User class. It will be 2 types of users:
    patient and doctor"""
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators=[phoneNumberRegex], max_length=16, blank=True, null=True)
    photo = models.ImageField(null=True, upload_to='mainApp/users/photos')
    date_of_birth = models.DateField(blank=True, null=True)
    is_doctor = models.BooleanField(blank=True, null=True)
    specialization = models.CharField(help_text="Doctor's specialization", max_length=30, blank=True, null=True)
    position = models.CharField(help_text="Doctor's position", max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        return str(self.username)

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Генерирует веб-токен JSON, в котором хранится идентификатор этого
        пользователя
        """
        token = jwt.encode({'id': self.pk}, SECRET_KEY, algorithm='HS256')

        return token


class Appointment(models.Model):
    """All information about visiting a doctor"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="+")
    doctor_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,  related_name="+")
    complaint = models.CharField(help_text="Patient's complaint(max 700 symbols)", max_length=700, blank=True)
    date = models.DateField(auto_now_add=True, null=True)

    PATIENT_STATUS = (
        ('i', 'Ill'),
        ('r', 'Recovering'),
        ('h', 'Healthy'),
    )

    status = models.CharField(max_length=1, choices=PATIENT_STATUS, blank=True, default="i")
    pathologies = models.CharField(max_length=150, help_text="Patient's pathologies", blank=True)
    disease = models.CharField(max_length=50, help_text="The diagnosis", blank=True)
    prescription = models.CharField(max_length=150, help_text="Doctor's prescription", blank=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return f"{str(self.user_id)}, {str(self.doctor_id)}"



class Analyzes(models.Model):
    name = models.CharField(blank=True, max_length=250)
    appointment_id = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True)
    analyze_doc = models.FileField(blank=True, upload_to='mainApp/users/analyzes')
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(self.name)
