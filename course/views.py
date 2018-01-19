from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from django.views.generic.edit import CreateView
from course.forms import StudentForm
from django.views.generic.list import ListView

from course.models import  Student

#def list_student(request, pk):
def list_student(request):
    student = Student.objects.all()
    return render(request, template_name='list_student.html', context={'student':student})


class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'add_student.html'

    def get_success_url(self):
        return reverse('course:list_student')