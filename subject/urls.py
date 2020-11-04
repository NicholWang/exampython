from django.urls import path
from .views import AddSubject, GetSubject


urlpatterns = [
    path('get_subject', GetSubject.as_view()),
    path('add_subject', AddSubject.as_view())
]