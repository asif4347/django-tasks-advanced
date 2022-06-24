from django.db import models
# from .project import urls as project_urls

# Create your models here.
from django.urls import reverse

"""
    Project
        TaskBoard
            Tasks

"""


class BaseModel(models.Model):
    title = models.CharField(max_length=100, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Project(models.Model):
    title = models.CharField(max_length=100, null=True, blank=False)
    description = models.TextField(max_length=200, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def edit_url(self):
        return reverse("update-projects", kwargs={"pk": self.pk})

    @property
    def delete_url(self):
        return reverse("delete-projects", kwargs={"pk": self.pk})


class TaskBoard(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False, blank=False,
                                related_name="taskboard_project")


class Task(BaseModel):
    TODO = "TODO"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    statuses = [
        (TODO, TODO),
        (PENDING, PENDING),
        (COMPLETED, COMPLETED),
    ]

    status = models.CharField(choices=statuses, null=False, default=TODO, max_length=15)
    task_board = models.ForeignKey(TaskBoard, on_delete=models.CASCADE, null=False, blank=False,
                                   related_name="task_taskboard")
