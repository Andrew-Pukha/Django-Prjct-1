from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _


# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )


# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)


#ОРИГИНАЛЬНЫЙ contact_page.html
#<!DOCTYPE html>
#<html>
#<head>
#<title>{{ flatpage.title }}</title>
#</head>
#<body>
#{{ flatpage.content }}
#{% include 'flatpages/inc.html' %}
#<h2> SKILL FACTORY </h2>
#</body>
#</html>