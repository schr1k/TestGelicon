from rest_framework import generics
from . import serializers
from .models import Performer, Task


class TasksList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer


class PerformersList(generics.ListCreateAPIView):
    queryset = Performer.objects.all()
    serializer_class = serializers.PerformerSerializer


class PerformerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Performer.objects.all()
    serializer_class = serializers.PerformerSerializer
