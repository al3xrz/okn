from django import forms
from .models import ObjectInfo
from django.contrib.admin import widgets
from . import models

class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ObjectInfoForm(forms.ModelForm):

    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget = widgets.AdminDateWidget()
    '''


    class Meta:
        model = ObjectInfo
        fields = '__all__'
        exclude = ('slug',)
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'}),
        }



