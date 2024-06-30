from django.urls import path
from .views import MaterialViewSet, MaterialDetailViewSet
urlpatterns = [
    path("materials/", MaterialViewSet.as_view()),
    path("materials/<int:pk>", MaterialDetailViewSet.as_view())
]
