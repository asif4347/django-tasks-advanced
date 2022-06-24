from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from ..models import Project
from . import tables as project_table
from . import urls as project_urls
from . import forms as project_forms
from . import utils as project_utils


def list_projects(request):
    queryset = Project.objects.all()
    table = project_table.ProjectTable(queryset)
    context = {
        "title": "List Projects",
        "table": table,
        "actions": [
            {
                "title": "Add Project",
                "href": project_urls.add_projects(),
                "classes": "btn btn-success",
                "icon": "fa fa-plus"
            },
            {
                "title": "Refresh",
                "href": project_urls.list_projects(),
                "classes": "btn btn-primary",
                "icon": "fa fa-sync"
            }
        ]
    }
    return render(request, "list-entries.html", context)


def add_project(request):
    form = project_forms.ProjectForm(request.POST or None)
    if request.method == "POST":
        form.save()
        return redirect(project_urls.list_projects())
    context = project_utils.get_project_context(form, project_urls.add_projects(), project_urls.list_projects(),
                                                "Add Project")
    return render(request, "add-update.html", context)


def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = project_forms.ProjectForm(request.POST or None, instance=project)
    if request.method == "POST":
        form.save()
        return redirect(project_urls.list_projects())
    context = project_utils.get_project_context(form, project_urls.update_projects(pk), project_urls.list_projects(),
                                                "Edit {}".format(project.title))
    return render(request, "add-update.html", context)


def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return JsonResponse({
        "success": True,
        "message": "Project deleted!"
    }, safe=False)
