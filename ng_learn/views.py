import generic as generic
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import *
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


# Create your views here.
class grouplist(ListView):
    model = group
    template_name = 'ng_learn/index.html'


# class groupdetail(ListView):
#     model = student
#     template_name = 'ng_learn/index.html'
#
#     def get_queryset(self):
#         return student.objects.order_by(groupname=self.kwargs['pk'])

class groupdetail(DetailView):
    queryset = group.objects.all()
    template_name = 'ng_learn/index.html'

def index(request):
    students = student.objects.all()
    num_student = student.objects.all().count()
    num_group = group.objects.all().count()
    context = {

        'students': students,
        'num_student': num_student,
        'num_group': num_group
    }
    return render(request, 'ng_learn/index.html', context)


def main(request):
    return HttpResponse("Глaвнaя страница")
