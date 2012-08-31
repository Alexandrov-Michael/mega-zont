#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# manage.py dumpscript bootstrap_tags

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

def run():
    from bootstrap_tags.models import ClearHtml

    cmsplugin_clearhtml_1 = ClearHtml()
    cmsplugin_clearhtml_1.parent = None
    cmsplugin_clearhtml_1.position = 1
    cmsplugin_clearhtml_1.language = u'ru'
    cmsplugin_clearhtml_1.plugin_type = u'ClearHtmlPlugin'
    cmsplugin_clearhtml_1.creation_date = datetime.datetime(2012, 8, 30, 11, 12, 9, 307947, tzinfo=<UTC>)
    cmsplugin_clearhtml_1.level = 0
    cmsplugin_clearhtml_1.lft = 1
    cmsplugin_clearhtml_1.rght = 2
    cmsplugin_clearhtml_1.tree_id = 3
    cmsplugin_clearhtml_1.text_f = u'<a href="/zakazat/" class=\'btn btn-primary btn-large\'><i class="icon-shopping-cart icon-white"></i> \u041a\u0443\u043f\u0438\u0442\u044c</a>'
    cmsplugin_clearhtml_1.save()

    cmsplugin_clearhtml_1.placeholder = Placeholder.objects.get(id=2)
    cmsplugin_clearhtml_1.cmsplugin_ptr = CMSPlugin.objects.get(id=3)
    cmsplugin_clearhtml_1.save()

