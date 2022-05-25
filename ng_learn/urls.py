from django.template.defaulttags import url
from django.urls import *
from ng_learn import views



urlpatterns = [
    path('learn/', views.main, name='learn'),
    path('', views.index, name='main'),
    path('groups/', views.grouplist.as_view(), name='groups'),
    path('groups/<int:pk>', views.groupdetail.as_view(), name='group-detail')
]