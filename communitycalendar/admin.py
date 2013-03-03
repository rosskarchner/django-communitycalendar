from django.contrib import admin
from .models import *


class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(SiteSettings)
admin.site.register(Group, GroupAdmin)
admin.site.register(Event)
