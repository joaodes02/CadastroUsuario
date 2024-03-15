from django.contrib import admin
from .models import usuario
from django.shortcuts import render


def __str__(self):
    return self.usuario

admin.site.register(usuario)
