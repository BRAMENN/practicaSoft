import datetime

from django.db import models as m

class Cliente(m.Model):
    DNI = m.CharField(verbose_name="documento", max_length=20,primary_key=True, blank=False, unique=True)
    name = m.CharField(verbose_name="nombre completo", max_length=200, blank=False)
    email = m.EmailField(verbose_name="Email",blank=False)
    birth = m.DateField(verbose_name="Fecha nacimineto", blank=False)
    creation_day = m.DateField(verbose_name="Fecha creacion",blank=False)
    imge = m.ImageField(verbose_name="foto")
