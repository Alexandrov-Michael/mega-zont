# -*- coding:utf-8 -*-

__author__ = 'michael'

from django.contrib import admin
import models


class OptionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'status_text', 'status_bool')
    list_display_links = list_display

admin.site.register(models.Options,OptionsAdmin)