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
    name = models.CharField(max_length=255,  help_text="фио студента", verbose_name="Фамилия и имя")
    otche = models.CharField(max_length=255, null=True, help_text="Отчество", verbose_name="Отчество")
    tel = models.IntegerField(help_text="номер телефона", verbose_name="телефон")
    email = models.CharField(max_length=50, null=True, help_text="эл. почта")
    predpay = models.BooleanField(default=False, null=True, help_text="предоплата", verbose_name="Предоплата")
    infomail = models.BooleanField(default=False, null=True, help_text="инф. письмо", verbose_name="Инф. письмо")
    balance = models.IntegerField(null=True, help_text="оплачено", verbose_name="Оплачено")
    predpay_summ = models.IntegerField(null=True, help_text="предоплата", verbose_name="Предоплата_сумма")
    ng_comment = models.TextField(blank=True, null=True, verbose_name="Заметки")
    groupname = models.ForeignKey('group', on_delete=models.PROTECT, related_name='students', null=True, verbose_name="Группа")
    psprt_sn = models.CharField(max_length=255, null=True, help_text="серия и номер", verbose_name="Серия и номер паспорта")
    psprt_issue = models.CharField(max_length=255, null=True, help_text="кем выдан", verbose_name="Кем выдан")
    psprt_date = models.CharField(max_length=255, null=True, help_text="когда выдан", verbose_name="Когда выдан")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])

    def get_debt(self):
        if self.groupname_id is None:
            return 0
        else:
            return self.groupname.price - self.balance


