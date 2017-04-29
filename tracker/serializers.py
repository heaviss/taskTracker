from tracker.models import Board, List, Project, Task, Subtask, Comment, Attachment
from rest_framework import serializers


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ('name', 'lists', 'background')


class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ('name', 'parent_board', 'position', 'projects', 'tasks', 'subtasks')
        depth = 1


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description', 'status', 'creation_date', 'arch_date', 'last_change_date',
                  'owner_list', 'tasks', 'attachments', 'comments')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'creation_date', 'arch_date', 'last_change_date',
                  'parent_project', 'owner_list', 'subtasks', 'attachments')


class SubtaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subtask
        fields = ('name', 'description', 'status', 'creation_date', 'arch_date', 'last_change_date',
                  'parent_task', 'owner_list', 'check_list')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('parent_project', 'author', 'creation_date', 'source', 'text')


class AttachmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attachment
        fields = ('project', 'task', 'name', 'file')
