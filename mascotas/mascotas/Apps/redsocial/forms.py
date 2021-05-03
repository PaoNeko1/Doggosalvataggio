from django import forms
from .models import Usuario, Pet, Comentario

class FormUsuarios(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'


class FormPet(forms.ModelForm):

    class Meta:
        model = Pet
        fields = '__all__'



class FormComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
    