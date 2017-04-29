# from django.shortcuts import render
# from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from tracker.models import Board, List, Project, Task, Subtask
from tracker.serializers import BoardSerializer, \
    ListSerializer, \
    ProjectSerializer, \
    TaskSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all().order_by('name')
    serializer_class = BoardSerializer


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all().order_by('name')
    serializer_class = ListSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class SubtaskViewSet(viewsets.ModelViewSet):
    queryset = Subtask.objects.all()
    serializer_class = Subtask
