from django import forms
from .models import Course, Student

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'duration']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'age', 'email', 'phone', 'course']