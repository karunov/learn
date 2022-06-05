# Create your views here.
import io

from django.conf import settings
from django.core.mail import send_mail
from django.db.models import F, Sum, Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone

from .forms import AddStudentForm, AddGroupForm, StudentModelForm
from .models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from docxtpl import DocxTemplate


# Create your views here.
# Главная страница
class IndexPage(ListView):
    model = group
    template_name = 'ng_learn/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexPage, self).get_context_data(**kwargs)

        context['students'] = student.objects.all()
        return context


# Подробности группы
class GroupDetail(DetailView):
    model = group
    template_name = 'ng_learn/group_detail.html'
    ordering = 'groupstart'

    # ost = student.objects.annotate(credit=F('groupname__price') - F('predpay_summ'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GroupDetail, self).get_context_data(**kwargs)
        now = timezone.now()
        # Список групп которые еще не прошли
        context['groups'] = group.objects.filter(groupstart__gte=now).order_by('groupstart')
        # узнаем количество студентов в выбранной группе
        count = student.objects.filter(groupname_id=self.kwargs['pk']).count()
        # вытаскиваем стоимость обучения в текущей группе
        prices = self.object.price
        # подсчитываем сумму оплаченную на данный момент студентами в выбранной группе
        studsum = student.objects.filter(groupname_id=self.kwargs['pk']).aggregate(Sum('balance'))
        if count > 0:
            # умножаем стоимость обучения на кол-во студентов
            multprice = prices * count
            # вычетаем из общей суммы - суммы оплат и получаем осток долга студентами в этой группе
            dolg = multprice - studsum['balance__sum']
            context['count'] = dolg
        else:
            context['count'] = '0'

        return context


class StudentDetail(DetailView):
    model = student
    template_name = 'ng_learn/student_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(StudentDetail, self).get_context_data(**kwargs)

        context['students'] = student.objects.all()
        return context


class StudentUpdate(UpdateView):
    form_class = StudentModelForm
    model = student
    template_name = 'ng_learn/student_edit.html'


    @property
    def success_url(self):
        return reverse('student-detail', args=(self.kwargs['pk'],))


def StudentDocx(request, pk):
    docpath = settings.BASE_DIR / 'ng_learn/templates/ng_learn/template_doc.docx'

    doc = DocxTemplate(docpath)
    #now = timezone.now()
    stud_contract = student.objects.get(pk=pk)
    contract_date = stud_contract.groupname.groupstart
    ps_sn = stud_contract.psprt_sn
    ps_date = stud_contract.psprt_date
    ps_issue = stud_contract.psprt_issue
    otch = stud_contract.otche
    tel = stud_contract.tel
    name = stud_contract.name

    print(contract_date)

    context = {'name': name,
               'contract_date': contract_date,
               'ps_sn': ps_sn,
               'ps_date': ps_date,
               'ps_issue': ps_issue,
               'otch': otch,
               'tel': tel
               }
    doc.render(context)

    file_stream = io.BytesIO()
    doc.save(file_stream)
    file_stream.seek(0)

    response = HttpResponse(file_stream.read())
    response["Content-Disposition"] = "attachment; filename=generated_doc.docx"
    response["Content-Type"] = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    return response


class GroupList(ListView):
    model = group
    template_name = 'ng_learn/group_list.html'

    def get_queryset(self):
        now = timezone.now()
        upcoming = group.objects.filter(groupstart__gte=now).order_by('groupstart')

        return upcoming


class ArhiveGroupList(ListView):
    model = group
    template_name = 'ng_learn/arh_group_list.html'

    def get_queryset(self):
        now = timezone.now()
        passed = group.objects.filter(groupstart__lte=now).order_by('groupstart')

        return passed


class StudentList(ListView):
    model = student
    template_name = 'ng_learn/student_list.html'
    # ordering = 'groupname__groupstart'
    ordering = 'name'


class StudentSearch(ListView):
    model = student
    template_name = 'ng_learn/student-search.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = student.objects.filter(
            Q(name__icontains=query) | Q(tel__icontains=query)
        )
        return object_list


class AddStudent(CreateView):
    form_class = AddStudentForm
    template_name = 'ng_learn/add_student.html'

    @property
    def success_url(self):
        return reverse('group-detail', args=(self.kwargs['pk'],))

    def form_valid(self, form):
        form.instance.groupname_id = self.kwargs['pk']
        form.instance.balance = form.cleaned_data['predpay_summ']
        return super().form_valid(form)


class DeleteStudent(DeleteView):
    model = student

    @property
    def success_url(self):
        if self.object.groupname is not None:
            return reverse('students')
            # return reverse('group-detail', args=(self.object.groupname_id,))
        else:
            return reverse('students')


def DelFromGroup(request, groupname_id, pk):
    delstudent = get_object_or_404(student, pk=pk, groupname_id=groupname_id)

    if request.method == "POST":
        delstudent.groupname = None
        delstudent.save()
        return redirect('group-detail', pk=groupname_id)


# class DeleteStudentFromGroup(DeleteView):
#     success_url = None
#
#     def delete(self, request, *args, **kwargs):
#         self.object.groupname = self.get_object()
#         success_url = self.get_success_url()
#         self.object.groupname = None
#         self.object.save()
#         return HttpResponseRedirect(success_url)
#
#     def post(self, request, *args, **kwargs):
#         return self.delete(request, *args, **kwargs)


class AddGroup(CreateView):
    form_class = AddGroupForm
    template_name = 'ng_learn/add_group.html'

    def form_valid(self, form):
        return super().form_valid(form)


class DeleteGroup(DeleteView):
    model = group
    success_url = reverse_lazy('groups')


send_mail(
    'Subject here',
    'Here is the message.',
    'tager3@mail.ru',
    ['karunov@list.ru'],
    fail_silently=False,
)
