from django.template.defaulttags import url
from django.urls import *
from ng_learn.views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('students/', StudentList.as_view(), name='students'),
    path('students/search', StudentSearch.as_view(), name='student-search'),
    path('students/<int:pk>', StudentDetail.as_view(), name='student-detail'),
    path('students/update/<int:pk>', StudentUpdate.as_view(), name='update-student'),
    path('students/<int:pk>/docx', StudentDocx, name='docx-student'),
    path('students/delete/<int:pk>', DeleteStudent.as_view(), name='delete-student'),
    path('groups/', GroupList.as_view(), name='groups'),
    path('groups/add-group/', AddGroup.as_view(), name='add-group'),
    path('groups/<int:pk>', GroupDetail.as_view(), name='group-detail'),
    path('groups/delete/<int:pk>', DeleteGroup.as_view(), name='delete-group'),
    path('groups/<int:pk>/add-student', AddStudent.as_view(), name='add-student'),
    path('groups/<int:groupname_id>/del-student-from-group/<int:pk>', DelFromGroup, name='del-from-group'),
    path('groups/arhive/', ArhiveGroupList.as_view(), name='arh-group')
]
