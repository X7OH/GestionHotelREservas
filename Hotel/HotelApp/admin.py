from django.contrib import admin
from .models import Usuario, Reservas, Habitacion

admin.site.register(Usuario)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'correo', 'Ciudad', 'rol')  # Campos visibles en la lista
    search_fields = ('nombre', 'correo')  # Habilita búsqueda por estos campos
    list_filter = ('rol', 'Ciudad')  # Habilita filtros por rol y Ciudad

admin.site.register(Usuario, UsuarioAdmin)

admin.site.register(Reservas)
class ReservasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'correo', 'piso', 'nhabitacion')  # Campos visibles en la lista
    search_fields = ('nombre', 'correo')  # Habilitar búsqueda
    list_filter = ('piso',)  # Filtros por piso

admin.site.register(Reservas, ReservasAdmin)

admin.site.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'piso', 'nhabitacion', 'Estado')  # Campos visibles en la lista
    search_fields = ('nhabitacion',)  # Búsqueda por número de habitación
    list_filter = ('Estado', 'piso')  # Filtros por estado y piso

admin.site.register(Habitacion, HabitacionAdmin)
