# -*- coding:utf-8 -*-

from django.http import Http404
from proj.utils.mixin import JSONResponseMixin
from django.views.generic.base import View
from models import Options


class ChangeKuponatorStatusView(JSONResponseMixin, View):
    """
    Ajax Представления для изменения статуса настройки купонатор
    """

    def get_context_data(self, **kwargs):
        """
        изменение статуса
        """
        self.check_for_admin()
        obj, created = Options.objects.get_or_create(name='kuponator')
        if created:
            status = False
            obj.discription = u'Булевное занчение, определяет режим купонатор или нет'
        else:
            status = obj.status_bool
        if status:
            obj.status_bool = False
            button_text  = u'Включить'
            button_class = 'btn btn-primary'
        else:
            obj.status_bool = True
            button_text = u'Отключить'
            button_class = 'btn btn-inverse'
        obj.save()
        return [button_text, button_class]

    def check_for_admin(self):
        user = self.request.user
        try:
            pk = user.pk
        except AttributeError:
            raise Http404
        if not pk == 1:
            raise Http404


ChangeKuponatorStatusView = ChangeKuponatorStatusView.as_view()


