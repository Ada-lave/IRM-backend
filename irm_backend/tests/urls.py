from django.urls import path
from .views import *
urlpatterns = [
    path(f"tests/<int:pk>", TestView.as_view()),
    path(f"tests/<int:pk>/check/", TestCheckView.as_view()),
    path(f"tests/", TestListView.as_view()),
    path(f"results/", ResultView.as_view()),
    path(f"results/export", ResultExportView.as_view())
]
