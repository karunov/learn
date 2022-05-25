from django.db import models

# Create your models here.
from django.urls import reverse


class group(models.Model):
    groupname = models.CharField(max_length=255, help_text="имя группы", verbose_name="название группы")
    groupstart = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True,
                                  help_text="дата начала обучения", verbose_name="Старт обучения")
    price = models.IntegerField(null=True, help_text="стоимость курса", verbose_name="стоимость курса")

    def __str__(self):
        return '%s %s' % (self.groupname, self.groupstart)

    def get_absolute_url(self):
        return reverse('group-detail', args=[str(self.id)])


class student(models.Model):
    name = models.CharField(max_length=255, help_text="фио студента")
    tel = models.IntegerField(max_length=30, help_text="номер телефона", verbose_name="телефон")
    email = models.CharField(max_length=50, null=True, help_text="эл. почта")
    predpay = models.BooleanField(default=False, null=True, help_text="предоплата", verbose_name="предоплата")
    infomail = models.BooleanField(default=False, null=True, help_text="инф. письмо", verbose_name="инф. письмо")
    balance = models.IntegerField(null=True, help_text="оплачено", verbose_name="оплачено")
    predpay_summ = models.IntegerField(null=True, help_text="предоплата", verbose_name="предоплата")
    ng_comment = models.TextField(blank=True, null=True)
    groupname = models.ForeignKey('group', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])
