from django.urls import path, reverse

from . import views as project_views

urlpatterns = [
    path("", project_views.list_projects, name="list-projects"),
    path("create", project_views.add_project, name="add-projects"),
    path("<int:pk>/update", project_views.edit_project, name="update-projects"),
    path("<int:pk>/delete", project_views.delete_project, name="delete-projects"),
]


def list_projects():
    return reverse("list-projects")


def add_projects():
    return reverse("add-projects")


def delete_projects(pk):
    return reverse("delete-projects", kwargs={"pk": pk})
