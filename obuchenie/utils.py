from .models import *

menu = [
    {'title': "Главная", 'url_name': "home"}

]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        groups = NG_course.objects.all()
        context['menu'] = menu
        context['groups'] = groups

        return context