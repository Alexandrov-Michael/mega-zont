# -*- coding:utf-8 -*-

__author__ = 'michael'

from django import forms
from options.models import Options


class SendForm(forms.Form):
    """
    Форма заказа

    """

    name = u'zakaz'

    def __init__(self, *args, **kwargs):
        super(SendForm, self).__init__(*args, **kwargs)
        try:
            status_cuponator = Options.objects.get(name='kuponator')
            if status_cuponator.status_bool:
                self.fields['kupon_number'] = forms.CharField(max_length=50, label=u'Номер купона')
        except Options.DoesNotExist:
            pass
        self.fields['email'] = forms.EmailField(label=u'E-mail')
        self.fields['comments'] = forms.CharField(label=u'Комментарии', widget=forms.Textarea())


    def get_name(self):
        """
        функция для шаблона для возврата имени формы
        """
        return self.name


#### Соответствия форм для модели и представления ######################



# Для представления
FORMS_MAPPING = {
        1 : SendForm,
    }


# Для модели
FORMS_CHOICE = (
        (1, 'Форма заказа'),
    )




###################################