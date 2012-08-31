#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# manage.py dumpscript myforms

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

def run():
    from myforms.models import FormLog

    myforms_formlog_1 = FormLog()
    myforms_formlog_1.email = u'koligin@mail.ru'
    myforms_formlog_1.comment = u'546456'
    myforms_formlog_1.date = datetime.datetime(2012, 8, 28, 20, 0, tzinfo=<UTC>)
    myforms_formlog_1.save()

    myforms_formlog_2 = FormLog()
    myforms_formlog_2.email = u'koligin345345@mail.ru'
    myforms_formlog_2.comment = u'345345345'
    myforms_formlog_2.date = datetime.datetime(2012, 8, 29, 11, 48, 8, 902154, tzinfo=<UTC>)
    myforms_formlog_2.save()

    myforms_formlog_3 = FormLog()
    myforms_formlog_3.email = u'koligin@mail.ru'
    myforms_formlog_3.comment = u'345'
    myforms_formlog_3.date = datetime.datetime(2012, 8, 30, 12, 17, 16, 148758, tzinfo=<UTC>)
    myforms_formlog_3.save()

    from myforms.models import FormLogPlugin

    cmsplugin_formlogplugin_1 = FormLogPlugin()
    cmsplugin_formlogplugin_1.parent = None
    cmsplugin_formlogplugin_1.position = 0
    cmsplugin_formlogplugin_1.language = u'ru'
    cmsplugin_formlogplugin_1.plugin_type = u'MyFormPlugin'
    cmsplugin_formlogplugin_1.creation_date = datetime.datetime(2012, 8, 29, 11, 30, 31, 24751, tzinfo=<UTC>)
    cmsplugin_formlogplugin_1.level = 0
    cmsplugin_formlogplugin_1.lft = 1
    cmsplugin_formlogplugin_1.rght = 2
    cmsplugin_formlogplugin_1.tree_id = 1
    cmsplugin_formlogplugin_1.form_number = 1
    cmsplugin_formlogplugin_1.save()

    cmsplugin_formlogplugin_1.placeholder = Placeholder.objects.get(id=4)
    cmsplugin_formlogplugin_1.cmsplugin_ptr = CMSPlugin.objects.get(id=1)
    cmsplugin_formlogplugin_1.save()

