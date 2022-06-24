def get_project_context(form, action_url, list_url, title):
    return {
        "title": title,
        "form": {
            "form": form,
            "action_url": action_url,
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
                        "value": list_url
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
