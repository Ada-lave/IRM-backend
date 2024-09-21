from django.urls import path
from .views import *
urlpatterns = [
    path(f"tests/<int:pk>", TestView.as_view()),
    path(f"tests/<int:pk>/check/", TestCheckView.as_view()),
    path(f"results/export", ResultView.as_view())
]
