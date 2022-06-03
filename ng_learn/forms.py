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
        exclude = ['predpay_summ']
        #fields = ['name', 'tel', 'email', 'predpay', 'infomail', 'balance', 'ng_comment', 'groupname']
        widgets = {
            'name': forms.TextInput(attrs={'size': 30}),
            'otche': forms.TextInput(attrs={'size': 36}),
            'tel': forms.TextInput(attrs={'size': 37}),
            'email': forms.TextInput(attrs={'size': 40}),
            'psprt_issue': forms.TextInput(attrs={'size': 40}),
            'psprt_sn': forms.TextInput(attrs={'size': 26}),
            'psprt_date': forms.TextInput(attrs={'size': 38}),
            'balance': forms.TextInput(attrs={'size': 12}),
            'ng_comment': forms.Textarea(attrs={'cols': 45, 'rows': 3})
        }