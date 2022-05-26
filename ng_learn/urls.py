from django.template.defaulttags import url
from django.urls import *
from ng_learn.views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('students/', StudentList.as_view(), name='students'),
    path('students/<int:pk>', StudentDetail.as_view(), name='student-detail'),
    path('groups/', GroupList.as_view(), name='groups'),
    path('groups/add-group/', AddGroup.as_view(), name='add-group'),
    path('groups/<int:pk>', GroupDetail.as_view(), name='group-detail'),
    path('groups/<int:pk>/add-student', AddStudent.as_view(), name='add-student')
]