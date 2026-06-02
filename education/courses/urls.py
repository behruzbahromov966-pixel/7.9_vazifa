from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<int:course_id>/', views.course_students, name='course_students'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/<int:course_id>/edit/', views.course_update, name='course_update'),
    path('courses/<int:course_id>/delete/', views.course_delete, name='course_delete'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:student_id>/edit/', views.student_update, name='student_update'),
    path('students/<int:student_id>/delete/', views.student_delete, name='student_delete'),
]