import django_tables2 as tables

from ..models import Project


class ProjectTable(tables.Table):
    actions = tables.Column(empty_values=())

    class Meta:
        attrs = {"class": "table"}
        model = Project
        fields = ["id", "title", "created_at", "actions"]
