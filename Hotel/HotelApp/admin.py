from django.contrib import admin
from .models import Usuario

admin.site.register(Usuario)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'correo', 'Ciudad', 'rol')  # Campos visibles en la lista
    search_fields = ('nombre', 'correo')  # Habilita búsqueda por estos campos
    list_filter = ('rol', 'Ciudad')  # Habilita filtros por rol y Ciudad

admin.site.register(Usuario, UsuarioAdmin)
