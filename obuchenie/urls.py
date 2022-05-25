from django.urls import path

from obuchenie import views
from obuchenie.views import *

urlpatterns = [
    path('', spisok_uchenikov.as_view(), name='home'),
    path('uchenik/<int:stroka_id>/', show_uchenik.as_view(), name='stroka'),
    path('group/<int:ng_gname>/', spisok_group.as_view(), name='group'),
    path('add/', add_uchenik.as_view(), name='add')

]

