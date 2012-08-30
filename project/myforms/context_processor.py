# -*- coding:utf-8 -*-

__author__ = 'michael'


def messages(request):
    """
    контектсный процессор для отрисовки особщений
    """
    result = {}
    result['message'] = request.session.pop('message', None)
    return result