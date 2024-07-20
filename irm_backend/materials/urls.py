from django.urls import path
from .views import MaterialViewSet, MaterialDetailViewSet, ThemeViewSet
urlpatterns = [
    path("materials/", MaterialViewSet.as_view()),
    path("materials/<int:pk>", MaterialDetailViewSet.as_view()),
    path("themes/", ThemeViewSet.as_view())
]
