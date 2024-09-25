from django.urls import path
from .views import *

urlpatterns = [
    path("materials/", MaterialViewSet.as_view()),
    path("materials/<int:pk>", MaterialDetailViewSet.as_view()),
    
    path("themes/", ThemeViewSet.as_view()),
    path("themes/<int:pk>", ThemeDetailViewSet.as_view()),
    
    path("departments/<int:pk>", DepartmentViewSet.as_view()),
    path("departments/", DepartmentViewSet.as_view()),
    
    path("sections/", SectionViewSet.as_view()),
    path("sections/<int:pk>", SectionViewSet.as_view()),
]
