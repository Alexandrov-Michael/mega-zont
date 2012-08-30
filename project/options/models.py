# -*- coding:utf-8 -*-

from django.db import models

class Options(models.Model):
    """
    Модель настроек
    """

    name        = models.CharField(max_length=50)
    status_text = models.CharField(max_length=100, blank=True)
    status_bool = models.BooleanField()
    discription = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
