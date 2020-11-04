from django.urls import path
from .views import AddClass, GetClass, DelClass, UpdateClass

urlpatterns = [
    path('add_class', AddClass.as_view()),
    path('get_class', GetClass.as_view()),
    path('del_class', DelClass.as_view()),
    path('update_class',UpdateClass.as_view())
]