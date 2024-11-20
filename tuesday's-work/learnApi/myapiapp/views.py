from django.shortcuts import render
from rest_framework import viewsets
from myapiapp.models import StudentInformation
from myapiapp.serializers import StudentSerializer

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentInformation.objects.all()
    serializer_class = StudentSerializer