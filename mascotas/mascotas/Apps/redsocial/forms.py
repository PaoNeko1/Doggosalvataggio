from django import forms
from .models import Usuario, Pet, Comenta


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
        model = Comenta
        fields = '__all__'
    