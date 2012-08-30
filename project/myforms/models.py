# -*- coding:utf-8 -*-

from django.db import models
from cms.models.pluginmodel import CMSPlugin
from forms import FORMS_CHOICE




class FormLogPlugin(CMSPlugin):
    """
    Модель для плагина django-cms
    """

    form_number = models.IntegerField(choices=FORMS_CHOICE)


class FormLog(models.Model):
    """
    Модель для логирования сообщений отпраленный с формы на сайте
    """

    email   = models.EmailField()
    comment = models.TextField()
    date    = models.DateTimeField()