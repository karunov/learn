from django import forms
from .models import *


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = student
        exclude = ['groupname']
        # fields = ['name', 'tel', 'email', 'predpay', 'infomail', 'balance', 'predpay_summ', 'ng_comment', 'groupname']


class AddGroupForm(forms.ModelForm):
    class Meta:
        model = group
        fields = ['groupname', 'groupstart', 'price']