import django_filters
from .models import Student


class StudentFilter(django_filters.FilterSet):
    CURSO_CHOICES = (
        ('i_1', 'Inicial 1'),
        ('i_2', 'Inicial 2'),
        ('i_3', 'Inicial 3')
    )

    curso = django_filters.ChoiceFilter(choices=CURSO_CHOICES)

    class Meta:
        model = Student
        fields = {
            'nombre': ['icontains']
        }



