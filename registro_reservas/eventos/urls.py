from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro_participantes/', views.registro_participantes, name='registro_participantes'),
    path('registro_evento/', views.registro_evento, name='registro_evento'),
    path('registro_exitoso/', views.registro_exitoso, name='registro_exitoso'),
]