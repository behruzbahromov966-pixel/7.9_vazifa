from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import Course, Student
from .forms import CourseForm, StudentForm

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

# Course CRUD ----------------------------------------------------------------
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Kurs muvaffaqiyatli qo'shildi!")
            return redirect('index')
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form, 'title': 'Yangi Kurs Qo\'shish'})


def course_update(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Kurs yangilandi!")
            return redirect('index')
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_form.html', {'form': form, 'title': 'Kursni Tahrirlash'})


def course_delete(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, "Kurs o'chirildi!")
        return redirect('index')
    return render(request, 'courses/course_confirm_delete.html', {'object': course})

# Student CRUD ----------------------------------------------------------------
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Talaba muvaffaqiyatli qo'shildi!")
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'courses/student_form.html', {'form': form, 'title': 'Yangi Talaba Qo\'shish'})


def student_update(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Talaba ma'lumotlari yangilandi!")
            return redirect('index')
    else:
        form = StudentForm(instance=student)
    return render(request, 'courses/student_form.html', {'form': form, 'title': 'Talabani Tahrirlash'})


def student_delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "Talaba o'chirildi!")
        return redirect('index')
    return render(request, 'courses/student_confirm_delete.html', {'object': student})