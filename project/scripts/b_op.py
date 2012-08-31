#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# manage.py dumpscript options

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

def run():
    from options.models import Options

    options_options_1 = Options()
    options_options_1.name = u'kuponator'
    options_options_1.status_text = u''
    options_options_1.status_bool = False
    options_options_1.discription = u'\u0411\u0443\u043b\u0435\u0432\u043d\u043e\u0435 \u0437\u0430\u043d\u0447\u0435\u043d\u0438\u0435, \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u0442 \u0440\u0435\u0436\u0438\u043c \u043a\u0443\u043f\u043e\u043d\u0430\u0442\u043e\u0440 \u0438\u043b\u0438 \u043d\u0435\u0442'
    options_options_1.save()

