from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200, verbose_name="Kurs nomi")
    description = models.TextField(blank=True, verbose_name="Tavsif")
    duration = models.IntegerField(help_text="Oylar soni", verbose_name="Davomiyligi")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"


class Student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')
    full_name = models.CharField(max_length=200, verbose_name="To'liq ism")
    age = models.IntegerField(verbose_name="Yosh")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefon")
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"