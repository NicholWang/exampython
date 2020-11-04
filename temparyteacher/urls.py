from django.urls import path
from .views import GetTempTeacher, AddTempTeacher, DelTempTeacher

urlpatterns = [
    path('get_tempteacher', GetTempTeacher.as_view()),
    path('add_tempteacher', AddTempTeacher.as_view()),
    path('del_tempteacher', DelTempTeacher.as_view())
]