from django.urls import path
from .views import SignView

urlpatterns = [
    path('sign', SignView.as_view())
]