from django.urls import path
from .views import CourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('add/', CourseCreateView.as_view(), name='course_add'),
    path('edit/<int:pk>/', CourseUpdateView.as_view(), name='course_edit'),
    path('delete/<int:pk>/', CourseDeleteView.as_view(), name='course_delete'),
]
