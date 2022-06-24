import django_tables2 as tables
from django.utils.html import format_html

from ..models import Project


class ProjectTable(tables.Table):
    actions = tables.Column(empty_values=())

    class Meta:
        attrs = {"class": "table data-table"}
        model = Project
        fields = ["id", "title", "created_at", "actions"]

    def render_id(self, value):
        return "#{}".format(value)

    def render_actions(self, record):
        return format_html("""
        <a class="btn btn-sm btn-outline-info" href="%s">Edit</a>
        <a onclick="show_swal(this)" data-url="%s" data-title="%s" class="btn btn-sm btn-outline-danger" href="%s">Delete</a>
        
        """ % (record.edit_url(), record.delete_url, record.title, "javascript:;"))
