from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Course, Student

def index(request):
    courses = Course.objects.all()
    students = Student.objects.all()
    context = {
        'courses': courses,
        'students': students,
    }
    return render(request, 'courses/index.html', context)


def course_students(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    students = course.students.all()
    context = {
        'course': course,
        'students': students,
    }
    return render(request, 'courses/course_students.html', context)


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    context = {
        'student': student,
    }
    return render(request, 'courses/student_detail.html', context)