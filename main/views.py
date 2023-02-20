from django.shortcuts import render
from rest_framework import viewsets
from main.serializers import StudentsSerializer
from .models import Student
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404


# Create your views here.

class StudentView(viewsets.ModelViewSet):
    # def list(self, request):
    #     queryset = Student.objects.all()
    #     serializer = StudentsSerializer(queryset, many=True)

    #     return Response(serializer.data)
        
    
    # def retrieve(self, request, pk=None):
    #     queryset = Student.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = StudentsSerializer(user)
    #     return Response(serializer.data)

    serializer_class = StudentsSerializer
    queryset = Student.objects.all()
