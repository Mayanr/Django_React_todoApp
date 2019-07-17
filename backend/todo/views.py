from django.shortcuts import render
# viewsets provides implementation for CRUD operations by default, 
from rest_framework import viewsets

from .serializers import TodoSerializer
from .models import Todo

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all() 