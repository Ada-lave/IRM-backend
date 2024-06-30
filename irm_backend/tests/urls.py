from django.urls import path
from .views import TestCheckView, TestView
urlpatterns = [
    path(f"tests/<int:pk>", TestView.as_view()),
    path(f"tests/<int:pk>/check/", TestCheckView.as_view()),
]
