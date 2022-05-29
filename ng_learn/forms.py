from django import forms
from django.forms import ModelForm

from .models import *


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = student
        exclude = ['groupname', 'balance']
        # fields = ['name', 'tel', 'email', 'predpay', 'infomail', 'balance', 'predpay_summ', 'ng_comment', 'groupname']


class AddGroupForm(forms.ModelForm):
    class Meta:
        model = group
        fields = ['groupname', 'groupstart', 'price']


class StudentModelForm(ModelForm):
    class Meta:
        model = student
        fields = ['name', 'tel', 'email', 'predpay', 'infomail', 'balance', 'predpay_summ', 'ng_comment', 'groupname']
