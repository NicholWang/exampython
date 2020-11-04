from django.urls import path
from .views import StudentLogin


urlpatterns = [
    path('studentlogin', StudentLogin.as_view())
]