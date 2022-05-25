from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from obuchenie.forms import add_uch_form
from obuchenie.models import *
from .utils import *



class spisok_uchenikov(DataMixin, ListView):
    model = NG_Groups
    template_name = 'obuchenie/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return NG_Groups.objects.all().order_by('ng_client')


# def index(request):
#    ucheniki = NG_Groups.objects.all()

#    context = {
#        'ucheniki': ucheniki,
#        'menu': menu,
#        'title': 'группы обучения',
#        'group_selected': 0,
#    }
#    return render(request, 'obuchenie/index.html', context=context)

# def show_uchenik(request, stroka_id):
#    uchenik = get_object_or_404(NG_Groups, pk=stroka_id)

#    context = {
#        'uchenik': uchenik,
#        'menu': menu,
#        'title': uchenik.ng_client,
#        'group_select': uchenik.ng_gname,
#    }

#    return render(request, 'obuchenie/uchenik.html', context=context)

class show_uchenik(DataMixin, DetailView):
    model = NG_Groups
    template_name = 'obuchenie/uchenik.html'
    context_object_name = 'uchenik'
    pk_url_kwarg = 'stroka_id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['uchenik'])
        return dict(list(context.items()) + list(c_def.items()))


# def show_group(request, ng_gname):
#    ucheniki = NG_Groups.objects.filter(ng_gname=ng_gname)

#    context = {
#        'ucheniki': ucheniki,
#        'menu': menu,
#        'group_select': ng_gname,
#    }
#    return render(request, 'obuchenie/index.html', context=context)

class spisok_group(DataMixin, ListView):
    model = NG_Groups
    template_name = 'obuchenie/index.html'
    context_object_name = 'groups'
    allow_empty = True

    def get_queryset(self):
        return NG_Groups.objects.filter(ng_gname=self.kwargs['ng_gname'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        group = context['groups'].first()
        if group:
            c_def = self.get_user_context(title=group.ng_gname, group_select=group.ng_gname_id)
            return dict(list(context.items()) + list(c_def.items()))


#def add_uchenik(request):
 #   if request.method == 'POST':
  #      form = add_uch_form(request.POST)
  ##          form.save()
  #          return redirect('home')
   # else:
  #      add_uch_form()
 #   return render(request, 'obuchenie/index.html', {'form': form, 'menu': menu})

class add_uchenik(DataMixin, CreateView):
    form_class = add_uch_form
    template_name = 'obuchenie/index.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление ученика")
        return dict(list(context.items()) + list(c_def.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")
