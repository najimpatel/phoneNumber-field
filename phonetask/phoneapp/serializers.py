from dataclasses import field
from xmlrpc.client import Server
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'phone_number', 'roll', 'city']
