# -*- coding:utf-8 -*-

from models import FormLog
from middleware import ForceResponse
from django.http import HttpResponseRedirect
from forms import FORMS_MAPPING
from datetime import datetime




def render(context, instance, placeholder):
    """
    Функция для рендернга плагина
    """
    result = Render_plugin(context, instance, placeholder)
    return result.render()




class Render_plugin(object):
    """
    Класс для рендеринда формы
    """

    def __init__(self, context, instance, placeholder ):
        self.context = context
        self.instance = instance
        self.placeholder = placeholder
        self.request = context['request']



    def render(self):
        """
        Рендеринг для шаблона в плагине
        """
        return self.dispath(self.request)


    def dispath(self, request):
        """
        Распердление по методам запроса
        """
        form_class = self.get_form_class()
        if request.method == 'POST':
            return self.post(request,form_class)
        if request.method == 'GET':
            return self.get(form_class)


    def post(self,request,form_class):
        """
        Метод пост
        """
        form = form_class(request.POST)
        return self.check_form(form)


    def get(self,form_class):
        """
        Метод гет
        """
        form = form_class()
        self.context.update({
            'form': form,
            })
        return self.context


    def get_form_class(self):
        """
        Плучение класса формы в зависимости от выбранного в плагине
        """
        form_number = self.instance.form_number
        return FORMS_MAPPING[form_number]


    def check_form(self, form):
        """
        Проверка на валидность формы
        """
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        """
        Если форма валидна
        """
        email   = form.cleaned_data['email']
        comment = form.cleaned_data['comments']
        self.create_email_log(email, comment)
        return self.form_success()


    def form_invalid(self, form):
        """
        Если форма заполнена не правильно то возвращаем ее обратно
        """
        self.context.update({
            'form': form,
            })
        return self.context


    def create_email_log(self, email, comment):
        """
        Создание объекта для логирования отпраленных сообщений
        """
        new_obj         = FormLog()
        new_obj.email   = email
        new_obj.comment = comment
        new_obj.date    = datetime.now()
        new_obj.save()


    def form_success(self):
        """
        Перенаправелние успено заполненной формы
        """
        url = self.request.META['PATH_INFO']
        text = u'Форма успешно отправлена.'
        self.set_message(text)
        raise ForceResponse(HttpResponseRedirect(url))


    def set_message(self, text):
        """
        Запись сообщения в сессию для последующего отображения в шаблоне через
        контекстный процессор
        """
        self.request.session['message'] = text













