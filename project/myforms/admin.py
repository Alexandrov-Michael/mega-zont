__author__ = 'michael'
from django.contrib import admin
import models



class FormLogAdmin(admin.ModelAdmin):
    list_display = ('date','email')
    list_display_links = list_display
    ordering = ['-date']

admin.site.register(models.FormLog, FormLogAdmin)