from django.contrib import admin
from django.urls import path
from app_study import views


urlpatterns = [
    #rota, view, nome
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('usuarios/',views.usuarios, name='listagem_usuarios')
]
