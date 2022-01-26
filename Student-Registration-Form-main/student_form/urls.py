from django.urls import path
from student_form import views


urlpatterns = [
    path("", views.home, name="home"),
    path("details/", views.student_details, name="student-details"),
    path("student_form", views.student_form, name="student-form"),
    path("students/<student_id>", views.list_students, name="student-list"),
    path("search_results/", views.search_students, name="search-student"),

   
]