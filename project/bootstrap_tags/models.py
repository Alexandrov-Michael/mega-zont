# -*- coding:utf-8 -*-

from django.db import models
from cms.models.pluginmodel import CMSPlugin


class ClearHtml(CMSPlugin):
    """
    Модель для вставки чистого html
    """
    text_f = models.TextField()

    class Meta:
        verbose_name = u'Чистый html'
        verbose_name_plural = u'Чистый html'


    def __unicode__(self):
        return u'ClearHtml'

