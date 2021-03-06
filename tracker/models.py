from django.db import models
from django.utils import timezone

from taggit.managers import TaggableManager

from django.db.models.signals import pre_save, post_init
from django.dispatch import receiver


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
    background = None  # todo models.ImageField()

    def __str__(self):
        return self.name


class List(models.Model):
    name = models.CharField(max_length=200)
    parent_board = models.ForeignKey(Board, related_name='lists', related_query_name='list')
    position = None

    def __str__(self):
        return self.name


class AbstractTask(models.Model):
    STATUSES = (
        ('A', 'Active'),
        ('D', 'Done'),
        ('P', 'Pause'),
        ('C', 'Cancelled')
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=1, choices=STATUSES, default='A')

    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    arch_date = models.DateTimeField(null=True, default=None, editable=False)
    last_change_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


    class Meta:
        abstract = True


class Project(AbstractTask):
    owner_list = models.ForeignKey(List, related_name='projects', related_query_name="project")
    # tags = TaggableManager()
    # comments = models.ManyToManyField(Comment)
    # check_lists


class Task(AbstractTask):
    parent_project = models.ForeignKey(Project, related_name='tasks', related_query_name="task", null=True)
    owner_list = models.ForeignKey(List, related_name='tasks', related_query_name="task")
    # tags = TaggableManager()

    # todo - repeat_period CommaSeparatedIntegerField ?
    # check_lists


class Subtask(AbstractTask):
    parent_task = models.ForeignKey(Task, related_name='subtasks', related_query_name="subtask")
    owner_list = models.ForeignKey(List, related_name='subtasks', related_query_name="subtask")
    check_list = TaggableManager()


class Comment(models.Model):
    parent_project = models.ForeignKey(Project, related_name='comments', related_query_name='comment')
    author = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    source = None
    text = models.TextField()

    def __str__(self):
        return self.text


class Attachment(models.Model):
    project = models.ForeignKey(Project, related_name='attachments', related_query_name="attachment")
    task = models.ForeignKey(Task, related_name='attachments', related_query_name="attachment")
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='attachments')

    def __str__(self):
        return self.name


@receiver(post_init)
def task_post_init_listener(sender, instance, **kwargs):
    if issubclass(sender, AbstractTask):
        instance._initial_status = instance.status


@receiver(pre_save)
def task_pre_save_listener(sender, instance, **kwargs):
    if issubclass(sender, AbstractTask):
        if instance._initial_status != instance.status:
            if instance.status in ('D', 'C'):
                instance.arch_date = timezone.now()
            else:
                instance.arch_date = None
