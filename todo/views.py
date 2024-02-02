from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


from todo.models import TODO
from .serializers import TodoSerializer

class TodoViewset(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TodoSerializer

