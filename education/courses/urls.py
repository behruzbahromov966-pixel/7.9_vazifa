from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<int:course_id>/', views.course_students, name='course_students'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
]