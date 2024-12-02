from django import forms
from HotelApp.models import Usuario
import re

class RegUs(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre','correo', 'contraseña','Ciudad']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }

    exp="^[a-zA-Z ]+$"
    expD="^[a-zA-Z0-9-]+$"
    
    def clean_nombre(self):
        nombre=self.cleaned_data.get('nombre')
        
        if not re.match(self.exp, nombre):
            raise forms.ValidationError("Verifica el Nombre no es un Nombre Válido")
        return nombre

    
    def clean_apellido(self):
        apellido=self.cleaned_data.get('apellido')
        if not re.match(self.exp, apellido):
            raise forms.ValidationError("Verifica el Apellido no es un Apellido Válido")
        return apellido

    
    def clean_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')
        if len(contraseña) < 8:
            raise forms.ValidationError("La contraseña debe ser de al menos 8 caracteres.")
        return contraseña

    
class LoginForm(forms.Form):
    correo = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo'}),
        max_length=254
    )
    contraseña = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}),
        max_length=128
    )

