from django.shortcuts import render
from app_list.models import student
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from app_list.serializers import studentSerializer,subjectSerializer


class SubjectView(APIView):
     serializer_class = subjectSerializer

     def post(self, request, format=None):
        serializer = subjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
class StudentView(APIView):
    serializer_class = studentSerializer
    # get all the student data from the data base 
    def get(self, request, format=None):
        snippets = student.objects.all()
        serializer = studentSerializer(snippets, many=True)
        return Response(serializer.data)

    # this will used to post the data into the database 
    def post(self, request, format=None):
        serializer = studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
