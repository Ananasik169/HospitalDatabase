from django.contrib import admin
from .models import Appointment, Analyzes, User


@admin.register(Analyzes)
class AnalyzesAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment_id', 'analyze_doc')
    fields = ['analyze_doc']
    list_filter = ('date',)


class AnalyzesInline(admin.TabularInline):
    model = Analyzes
    fields = ['id', 'analyze_doc']
    extra = 0


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id',  'doctor_id',  'user_id', 'disease', )

    fieldsets = (
        (None, {
            'fields': (('user_id', 'doctor_id'),)
        }),
        ('Disease information', {
            'fields': ('status',  'complaint', 'pathologies', 'disease', 'prescription')
        }),
    )

    list_filter = ('date', 'status', 'doctor_id', 'user_id')
    inlines = [AnalyzesInline]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
