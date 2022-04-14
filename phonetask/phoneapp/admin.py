from django.contrib import admin

from . models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_number', 'roll', 'city']
