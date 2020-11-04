from django.urls import path
from .views import LoginView

urlpatterns = [
    path('teacherlogin', LoginView.as_view())
]