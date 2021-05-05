from django.urls import path
from . import views

urlpatterns = [
    # ex: /encuestas/
    path('home', views.index, name='index'),
    path('base/', views.base, name='base_generic'),
    path('index/', views.inicio, name='inicio'),

    path('college/', views.college, name='college'),
    path('veterinarios/', views.veterinarios, name='veterinarios'),
    path('implementos/', views.animalcosas, name='animalcosas'),

	path('res/<rut>/<color>/', views.resultado ),
	path('res/<rut>/<color>/<nombrep>', views.eliminarp ),
	path('registrar/', views.registrar ),
<<<<<<< HEAD
=======
	path('comentar/', views.comentar ),
    path('testimonio/', views.testimonio, name='testimonio'),
>>>>>>> fb69ba154345f882e50b4df350155a981e19c776
    path('contacto/', views.contacto, name='contacto'),
    path('formulario/', views.usuario, name='formulario'),
    path('login/', views.login, name='login'),
    path('usuario/', views.pet_form, name='usuario'),
    path('comentario/', views.comentario_form, name='comentario')
    
    
]

