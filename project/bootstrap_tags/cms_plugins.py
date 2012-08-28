# -*- coding:utf-8 -*-

__author__ = 'michael'


from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from models import ClearHtml

class ClearHtmlPlugin(CMSPluginBase):
    model = ClearHtml
    name = u'Чистый html'
    render_template = "clear_html.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(ClearHtmlPlugin)