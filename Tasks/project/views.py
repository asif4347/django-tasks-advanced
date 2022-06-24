from django.shortcuts import render, redirect

from ..models import Project
from . import tables as project_table
from . import urls as project_urls
from . import forms as project_forms


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
    context = {
        "title": "Add Project",
        "form": {
            "form": form,
            "action_url": project_urls.add_projects(),
            "method": "post"
        },
        "actions": [
            {
                "tag": "a",
                "title": "Back",
                "attrs": [
                    {
                        "name": "class",
                        "value": "btn btn-danger"
                    }, {
                        "name": "href",
                        "value": project_urls.list_projects()
                    }
                ],
                "icon": "fa fa-back-arrow"
            }, {
                "tag": "button",
                "title": "Submit",
                "attrs": [
                    {
                        "name": "class",
                        "value": "btn btn-success"
                    }, {
                        "name": "type",
                        "value": "submit"
                    }
                ],
                "icon": "fa fa-plus"
            },
        ]
    }
    return render(request, "add-update.html", context)
