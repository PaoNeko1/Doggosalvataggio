from django.urls import path
from . import views

urlpatterns = [
    # ex: /encuestas/
    path('home', views.index, name='index'),
    path('base/', views.base, name='base_generic'),
    path('index/', views.inicio, name='inicio'),
    path('college/', views.college, name='college'),
    path('testimonio/', views.testimonio, name='testimonio'),
    path('contacto/', views.contacto, name='contacto'),
    path('formulario', views.usuario, name='formulario'),
    path('login', views.login, name='login')
]