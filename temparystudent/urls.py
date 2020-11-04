from django.urls import path
from .views import GetTempStu, AddTempStu, DelTempStu


urlpatterns = [
    path('get_tempstu', GetTempStu.as_view()),
    path('add_tempstu', AddTempStu.as_view()),
    path('del_tempstu', DelTempStu.as_view())
]