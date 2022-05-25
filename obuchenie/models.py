from django.db import models

# Create your models here.
from django.urls import reverse


class NG_Groups(models.Model):
    ng_client = models.CharField(max_length=255)
    ng_tel = models.CharField(max_length=20)
    ng_email = models.CharField(max_length=50)
    ng_predpay = models.BooleanField(default=False)
    ng_pismo = models.BooleanField(default=False)
    ng_balance = models.IntegerField()
    ng_predpay_summ = models.IntegerField()
    ng_comment = models.TextField(blank=True)
    ng_gname = models.ForeignKey('NG_course', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.ng_client

    def get_absolute_url(self):
        return reverse('stroka', kwargs={'stroka_id': self.pk})

    class Meta:
        verbose_name = 'список учеников'
        verbose_name_plural = 'список учеников'
        ordering = ['id']

class NG_course(models.Model):
    ng_groupname = models.CharField(max_length=100, db_index=True)
        ng_start = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.ng_groupname

    def get_absolute_url(self):
        return reverse('group', kwargs={'ng_gname': self.pk})

    class Meta:
        verbose_name = 'список групп'
        verbose_name_plural = 'список групп'
        ordering = ['ng_start']