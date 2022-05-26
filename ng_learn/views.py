# Create your views here.
from django.template import RequestContext
from django.urls import reverse_lazy

from .forms import AddStudentForm, AddGroupForm
from .models import *
from django.views.generic import ListView, DetailView, CreateView


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GroupDetail, self).get_context_data(**kwargs)

        context['groups'] = group.objects.all()
        return context


class StudentDetail(DetailView):
    model = student
    template_name = 'ng_learn/student_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(StudentDetail, self).get_context_data(**kwargs)

        context['students'] = student.objects.all()
        return context


class GroupList(ListView):
    model = group
    template_name = 'ng_learn/group_list.html'


class StudentList(ListView):
    model = student
    template_name = 'ng_learn/student_list.html'


class AddStudent(CreateView):
    form_class = AddStudentForm
    template_name = 'ng_learn/add_student.html'

    @property
    def success_url(self):
        return reverse('group-detail', args=(self.kwargs['pk'],))

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.instance.groupname_id = self.kwargs['pk']
        return super().form_valid(form)


class AddGroup(CreateView):
    form_class = AddGroupForm
    template_name = 'ng_learn/add_group.html'

    def form_valid(self, form):
        return super().form_valid(form)
