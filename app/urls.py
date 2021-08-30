from .views import *
from django.urls import path
#api application urls ...
urlpatterns = [
    path('student/', StudentsView.as_view(), name="studentsview"),           #all the students details using GET.
    path('student/<int:pk>/marks/add/', AddMarks.as_view(), name="addstudsmarks"),  #add marks particular student using POST
    path('student/<int:pk>/marks/', ParticularStudentMarks.as_view(), name="particularstudentmark"),   #particular student mark using GET
    path('student/marks/', MarkAllStudents.as_view(), name="markofallstudents"),           #mark of all students GET
    path('student/results/', StudentsResults.as_view(), name="studentsresult"),           #category based student results
]