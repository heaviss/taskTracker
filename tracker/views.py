# from django.shortcuts import render
# from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from tracker.models import Board, List, Project, Task, Subtask, Attachment, Comment
import tracker.serializers as ts


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all().order_by('name')
    serializer_class = ts.BoardSerializer


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all().order_by('name')
    serializer_class = ts.ListSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ts.ProjectSerializer



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = ts.TaskSerializer


class SubtaskViewSet(viewsets.ModelViewSet):
    queryset = Subtask.objects.all()
    serializer_class = ts.SubtaskSerializer

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = ts.AttachmentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = ts.CommentSerializer