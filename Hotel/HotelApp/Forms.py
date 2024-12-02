from django import forms
from HotelApp.models import Usuario, Habitacion, Reservas
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

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        # Validación personalizada si es necesario, por ejemplo, formato adicional
        if not re.match(r"^[^@]+@[^@]+\.[^@]+$", correo):
            raise forms.ValidationError("Ingrese un correo válido.")
        return correo

    def clean_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')
        if len(contraseña) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return contraseña
    
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = ['nombre', 'correo', 'contraseña', 'piso', 'nhabitacion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo'}),
            'contraseña': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
            'piso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Piso'}),
            'nhabitacion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de Habitación'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not re.match(r'^[a-zA-Z ]+$', nombre):
            raise forms.ValidationError("El nombre solo puede contener letras y espacios.")
        return nombre

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if not re.match(r'^\S+@\S+\.\S+$', correo):
            raise forms.ValidationError("Por favor, ingresa un correo válido.")
        return correo

    def clean_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')
        if len(contraseña) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return contraseña

    def clean(self):
        cleaned_data = super().clean()
        piso = cleaned_data.get('piso')
        nhabitacion = cleaned_data.get('nhabitacion')

        if piso <= 0:
            raise forms.ValidationError("El número de piso debe ser mayor a 0.")
        if nhabitacion <= 0:
            raise forms.ValidationError("El número de la habitación debe ser mayor a 0.")
        


class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['piso', 'nhabitacion', 'Estado']
        widgets = {
            'piso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Piso'}),
            'nhabitacion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de Habitación'}),
            'Estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_piso(self):
        piso = self.cleaned_data.get('piso')
        if piso <= 0:
            raise forms.ValidationError("El número de piso debe ser mayor a 0.")
        return piso

    def clean_nhabitacion(self):
        nhabitacion = self.cleaned_data.get('nhabitacion')
        if nhabitacion <= 0:
            raise forms.ValidationError("El número de la habitación debe ser mayor a 0.")
        return nhabitacion