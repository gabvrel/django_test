from django.urls import path
from .views import PostStudents, ProfileStudent, CreateStudentView
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', PostStudents.as_view(), name='student-view'),
    path('<int:pk>/', ProfileStudent.as_view(), name='student-profile'),
    path('create/', CreateStudentView.as_view(), name='student-create')
]

