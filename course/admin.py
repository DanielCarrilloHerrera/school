from django.contrib import admin
from course.models import Subject, Student
# Register your models here.


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_credits')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name')


admin.site.register(Student, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)