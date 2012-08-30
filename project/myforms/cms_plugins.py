# -*- coding:utf-8 -*-

__author__ = 'michael'


from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from models import FormLogPlugin
from views import render



from django.http import HttpResponseRedirect


class MyFormPlugin(CMSPluginBase):
    """
    Плагин для django-cms
    """
    model = FormLogPlugin
    name  = u'Пользовательские формы'
    render_template = "myform.html"

    def render(self, context, instance, placeholder):
        return render(context, instance, placeholder)

plugin_pool.register_plugin(MyFormPlugin)
