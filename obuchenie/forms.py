from django import forms
from .models import *


class add_uch_form(forms.ModelForm):
    class Meta:
        model = NG_Groups
        fields = ['ng_client', 'ng_tel', 'ng_email', 'ng_predpay', 'ng_pismo', 'ng_balance', 'ng_predpay_summ', 'ng_comment', 'ng_gname']
