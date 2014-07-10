# coding=utf-8

from django.contrib import admin
from adminsortable.admin import SortableTabularInline, SortableAdmin
from .models import SaltCommand, SaltArg


class SaltArgInline(SortableTabularInline):
    model = SaltArg
    extra = 1


class SaltCommandAdmin(SortableAdmin):
    inlines = [SaltArgInline]
    list_display = ['name', 'key', 'salt_target', 'salt_function']

admin.site.register(SaltCommand, SaltCommandAdmin)
