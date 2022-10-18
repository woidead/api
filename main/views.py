from asyncio import queues
from django.shortcuts import render
from main.serializers import StudentsSerilazer
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView 
from main.models import *
# Create your views here.

class AboutStudents(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = StudentsSerilazer

    def get_queryset(self):
        queryset = Students.objects.all()
        return queryset        
    def get(self, requst):
        return self.list(requst)
    
    def post(self, request, format = None):
        return self.create(request)




