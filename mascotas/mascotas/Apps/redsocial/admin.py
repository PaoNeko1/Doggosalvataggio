from django.contrib import admin

# Register your models here.
from .models import Usuario
from .models import Pet

admin.site.register(Usuario)
admin.site.register(Pet)