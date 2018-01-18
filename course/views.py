from django.shortcuts import render
from course.models import  Student
# Create your views here.
def list_student(request, pk):
    student = Student.objects.all()
    return render(request, template_name='list_student.html', context={'student':student})
