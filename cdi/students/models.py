from django.db import models
from django.core.validators import MaxValueValidator
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse
import math
from PIL import Image


class Student(models.Model):
    COURSE_CHOICES = [('i_1', 'Inicial 1'), ('i_2', 'Inicial 2'), ('i_3', 'Inicial 3')]
    SEX_CHOICE = [('m', 'Masculino'), ('f', 'Femenino')]
    RACE_CHOICE = [('blanca', 'Blanca'), ('meztiza', 'Mestiza'), ('negra', 'Afrodescendiente'), ('indigena', 'Indigena')]
    MOTHER_BIRTH_BEHAVIOUR = [('normal', 'Normal'), ('complicado', 'Complicado')]
    DISABILITY_CHOICE = [('fisica', 'Fisica'), ('mental', 'Mental')]
    CIVIL_STATE = [('soltero/a', 'Soltero/a'), ('casado/a', 'Casado/a')]

    nombre = models.CharField(max_length=130)
    foto = models.ImageField(default='default.jpg', upload_to='students_pics', blank=True)
    sexo = models.CharField(max_length=130, choices=SEX_CHOICE)
    raza = models.CharField(max_length=120, choices=RACE_CHOICE)
    fecha_de_nacimiento = models.DateField(default=datetime.now(), help_text='Año-Mes-Dia', blank=True, null=True)
    ci = models.PositiveSmallIntegerField(unique=True, validators=[MaxValueValidator(9999999999)])
    nacionalidad = models.CharField(max_length=130, default='Ecuatoriana')
    curso = models.CharField(max_length=130, choices=COURSE_CHOICES, blank=True)
    domicilio = models.TextField()
    embarazo_de_la_madre_con_control = models.BooleanField(default=True, blank=True)
    parto_de_la_madre = models.CharField(max_length=120, choices=MOTHER_BIRTH_BEHAVIOUR, blank=True)
    tiene_discapacidad = models.BooleanField(default=False)
    tipo_de_discapacidad = models.CharField(max_length=125, choices=DISABILITY_CHOICE, blank=True)
    parte_afectada_por_discapacidad = models.CharField(max_length=130, blank=True)
    tipo_de_alimentacion = models.CharField(max_length=130)
    desde_que_edad_comio_solidos = models.FloatField(default=3)
    hasta_que_edad_tomo_leche_materna = models.FloatField(default=3)
    tipo_de_sangre = models.CharField(max_length=125)
    alergias = models.TextField(blank=True)
    enfermedades = models.TextField(blank=True)
    operaciones = models.TextField(blank=True)
    profesora = models.ForeignKey(User, on_delete=models.CASCADE)

    nombre_del_representante = models.CharField(max_length=130)
    ci_del_representante = models.PositiveSmallIntegerField()
    nacionalidad_del_representante = models.CharField(max_length=130, default='Ecuatoriana')
    telefono_del_representante = models.IntegerField()
    estado_civil_del_representante = models.CharField(max_length=125, choices=CIVIL_STATE, blank=True)
    representante_vive_con_estudiante = models.BooleanField()
    domicilio_del_representante = models.TextField(blank=True)
    lugar_trabajo_del_representante = models.TextField(blank=True)
    el_representante_es_el_padre_o_la_madre = models.BooleanField(default=True)

    nombre_de_la_madre = models.CharField(max_length=130, blank=True)
    ci_de_la_madre = models.PositiveSmallIntegerField(blank=True)
    nacionalidad_de_la_madre = models.CharField(max_length=130, default='Ecuatoriana', blank=True)
    telefono_de_la_madre = models.IntegerField()
    estado_civil_de_la_madre = models.CharField(max_length=125, choices=CIVIL_STATE, blank=True)
    madre_vive_con_hijo = models.BooleanField(default=True, blank=True)
    domicilio_de_la_madre = models.TextField(blank=True)
    lugar_trabajo_de_la_madre = models.TextField(blank=True)

    nombre_del_padre = models.CharField(max_length=130, blank=True)
    ci_del_padre = models.PositiveSmallIntegerField(blank=True)
    nacionalidad_del_padre = models.CharField(max_length=130, default='Ecuatoriana', blank=True)
    telefono_del_padre = models.IntegerField(blank=True)
    estado_civil_de_padre = models.CharField(max_length=125, choices=CIVIL_STATE, blank=True)
    padre_vive_con_hijo = models.BooleanField(default=True)
    domicilio_del_padre = models.TextField(blank=True)
    lugar_trabajo_del_padre = models.TextField(blank=True)

    documentos_adjuntos = models.FileField(blank=True, null=True, upload_to='atachdocs/%Y/%m/%D/')

    def __str__(self):
        return str(self.nombre) + ' ' + str(self.curso)

    @property
    def age(self):
        age_year = int((datetime.now().date() - self.fecha_de_nacimiento).days / 365.25)
        return age_year

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.foto.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.foto.path)



