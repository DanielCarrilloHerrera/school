from django.conf.urls import url
from course import views

urlpatterns = [
    url(r'^list_student/', views.list_student, name='list_student'),

]
