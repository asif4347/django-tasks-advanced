from django.urls import path, reverse

from . import views as project_views

urlpatterns = [
    path("", project_views.list_projects, name="list-projects"),
    path("create", project_views.add_project, name="add-projects"),
]


def list_projects():
    return reverse("list-projects")


def add_projects():
    return reverse("add-projects")
