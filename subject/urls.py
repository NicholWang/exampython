from django.urls import path
from .views import AddSubject


urlpatterns = [
    path('add_subject', AddSubject.as_view())
]