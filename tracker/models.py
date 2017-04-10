from django.db import models
#from django.utils import timezone

from taggit.managers import TaggableManager

'''
1.Доска. У неё будут заголовок, листы, фоновый рисунок:)
2.Лист. У него - имя, доска-хозяйка, позиция на доске, проекты, задачи, подзадачи

3. Абстрактная задача: имя, дата создания, лист-владелец, описание, статус(активна/выполнена/отложена, отменена),
    дата архивации, дата изменения

3.1. Проект - штуковина для выполнения дел, в которых больше одной задачи. В нём -  
    вложения, тэги, чек-листы - списки задач, комментарии, 

3.2. Задача - проект-предок(если есть), периодичность(если есть), вложения, тэги, 
    чек-листы - списки подзадач

3.3. Подзадача - создается только из чек-листа задачи. Урезанная. В ней - задача-предок, чек-листы - просто списки

4. Комментарий - автор, дата создания, откуда пришел, текст

5. Вложение: имя, ссылка на файл
'''

class Board(models.Model):
    name = models.CharField(max_length=200)
    lists = models.ManyToManyField(List)
    background = models.ImageField()

class List(models.Model):
    name = models.CharField(max_length=200)
    parent_board = models.ForeignKey(Board)
    position = None #todo
    projects = models.ManyToManyField(Project)
    tasks = models.ManyToManyField(Task)
    subtasks = models.ManyToManyField(Subtask)

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

    creation_date = models.DateTimeField(auto_now_add=True)
    arch_date = models.DateField(default=None)
    last_change_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Project(AbstractTask):
    parent_list = models.ForeignKey(List)
    attachments = models.ManyToManyField(Attachment)
    tags = TaggableManager()
    tasks = models.ManyToManyField(Task)
    #comments = models.ManyToManyField(Comment)
    #check_lists


class Task(AbstractTask):
    parent_project = models.ForeignKey(Project)
    #todo - repeat_period
    attachments = models.ManyToManyField(Attachment)
    tags = TaggableManager()
    #check_lists


class Subtask(AbstractTask):
    parent_task = models.ForeignKey(Task)
    check_list = TaggableManager()


class Comment(models.Model):
    author = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    source = None
    text = models.TextField()

class Attachment(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='attachments')