from django.conf.urls import url
from course import views

app_name="course"

urlpatterns = [
    url(r'^list_student/', views.list_student, name='list_student'),
    url(r'^create_student/', views.StudentCreate.as_view(), name="create_student")
]
