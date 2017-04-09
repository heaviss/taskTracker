from django.db import models
from django.utils import timezone

'''
1. Доска. У неё будут заголовок, листы, фоновый рисунок:)
2. Лист. У него - имя, доска-хозяйка, позиция на доске, проекты, задачи, подзадачи
3. Проект - штуковина для выполнения дел, в которых больше одной задачи. В нём - имя, дата создания, лист-хозяин, описание, статус, вложения, дата архивации, тэги, чек-листы - списки задач, комментарии, дата изменения
4. Задача - имя, дата создания, лист-хозяин, проект-хозяин(если есть), описание, статус(активна/выполнена/отложена, отменена), периодичность(если есть), вложения, дата архивации, тэги, чек-листы - списки подзадач, дата изменения
5. Подзадача - создается только из чек-листа задачи. Урезанная. В ней - имя, дата создания, лист-хозяин, задача-хозяйка, описание, статус, дата архивации, тэги, чек-листы - просто списки, дата изменения
6. Комментарий - автор, дата создания, откуда пришел, текст
'''

class Board(models.Model):
    name = models.CharField(max_length=200)
    lists = None
    background = models.ImageField()

class List(models.Model):
    name = models.CharField(max_length=200)
    parent_board = models.ForeignKey(Board)
    position = None
    projects = []
    tasks = []
    subtasks = []

class AbstractTask(models.Model):
    STATUSES = (
        ('A', 'Active'),
        ('D', 'Done'),
        ('P', 'Pause'),
        ('C', 'Cancelled')
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUSES)

    #dates
    creation_date = models.DateTimeField(auto_now_add=True)
    arch_date = models.DateField(default=None)
    last_change_date = models.DateField(auto_now=True)


    class Meta:
        abstract = True


class Project(AbstractTask):

    parent_list = models.ForeignKey(List)
    #attachments = models.FileField(upload_to='uploads/')
    #tags
    #checklists
    #comments


class Task(AbstractTask):
    pass

class Subtask(AbstractTask):
    pass

class Comment(models.Model):
    name = models.CharField(max_length=200)
    pass