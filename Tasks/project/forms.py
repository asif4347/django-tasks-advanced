from django import forms

from ..models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"data_icon": "fa fa-user", "col_cls": "col-md-8"}),
            "description": forms.Textarea(attrs={"data_icon": "fa fa-hashtag","col_cls": "col-md-12"}),
        }
