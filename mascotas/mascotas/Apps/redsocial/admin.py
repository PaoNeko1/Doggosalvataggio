from django.contrib import admin

# Register your models here.
from .models import Usuario
from .models import Pet
from .models import Comentario

admin.site.register(Usuario)
admin.site.register(Pet)
admin.site.register(Comentario)