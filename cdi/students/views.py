from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Student
from django.urls import reverse
from .filters import StudentFilter


class PostStudents(ListView):
    model = Student
    template_name = 'students/students_list.html'
    context_object_name = 'students'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = StudentFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ProfileStudent(DetailView):
    model = Student
    context_object_name = 'students'


class CreateStudentView(LoginRequiredMixin, CreateView):
    model = Student
    fields = '__all__'

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('student-view')



