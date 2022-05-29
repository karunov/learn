# Create your views here.
from django.db.models import F, Sum, Q
from django.http import StreamingHttpResponse
from django.urls import reverse_lazy
from .forms import AddStudentForm, AddGroupForm
from .models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from docxtpl import DocxTemplate

# Create your views here.

class IndexPage(ListView):
    model = group
    template_name = 'ng_learn/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexPage, self).get_context_data(**kwargs)

        context['students'] = student.objects.all()
        return context


class GroupDetail(DetailView):
    model = group
    template_name = 'ng_learn/group_detail.html'
    ordering = 'groupstart'

    # ost = student.objects.annotate(credit=F('groupname__price') - F('predpay_summ'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GroupDetail, self).get_context_data(**kwargs)
        context['groups'] = group.objects.all()
        #узнаем количество студентов в выбранной группе
        count = student.objects.filter(groupname_id=self.kwargs['pk']).count()
        #вытаскиваем стоимость обучения в текущей группе
        prices = self.object.price
        #подсчитываем сумму оплаченную на данный момент студентами в выбранной группе
        studsum = student.objects.filter(groupname_id=self.kwargs['pk']).aggregate(Sum('balance'))
        #умножаем стоимость обучения на кол-во студентов
        multprice = prices * count
        #вычетаем из общей суммы - суммы оплат и получаем осток долга студентами в этой группе
        dolg = multprice - studsum['balance__sum']
        context['count'] = dolg
        return context



class StudentDetail(DetailView):
    model = student
    template_name = 'ng_learn/student_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(StudentDetail, self).get_context_data(**kwargs)

        context['students'] = student.objects.all()
        return context


class StudentUpdate(UpdateView):
    model = student
    fields = '__all__'

    # success_url = reverse_lazy('student-detail')

    @property
    def success_url(self):
        return reverse('student-detail', args=(self.kwargs['pk'],))


class GroupList(ListView):
    model = group
    template_name = 'ng_learn/group_list.html'
    ordering = 'groupstart'


class StudentList(ListView):
    model = student
    template_name = 'ng_learn/student_list.html'
    ordering = 'groupname__groupstart'

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
        return reverse('group-detail', args=(self.object.groupname_id,))


class AddGroup(CreateView):
    form_class = AddGroupForm
    template_name = 'ng_learn/add_group.html'

    def form_valid(self, form):
        return super().form_valid(form)


class DeleteGroup(DeleteView):
    model = group
    success_url = reverse_lazy('groups')
