from django import forms
from .models import Usuario, Pet

class FormUsuarios(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'


class FormPet(forms.ModelForm):

    class Meta:
        model = Pet
        fields = '__all__'