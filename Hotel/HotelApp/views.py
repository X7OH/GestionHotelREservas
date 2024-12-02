from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from django.utils.decorators import method_decorator
import json
from HotelApp.models import Usuario, Reservas,Habitacion 
from HotelApp.Forms import RegUs

from django.http import JsonResponse

def home(request):
    rol = request.session.get('usuario_rol', None)
    correo = request.session.get('usuario_correo', None)
    return JsonResponse({
        'message': 'Bienvenido a la API de Tienda Mascota',
        'user_role': rol,
        'user_email': correo
    })


@csrf_exempt
def Registro(request):
    if request.method == "POST":
        try:
            # Parsear el cuerpo de la solicitud como JSON
            data = json.loads(request.body)

            # Crear instancia del formulario usando los datos JSON
            form = RegUs(data)
            if form.is_valid():
                usuario = form.save(commit=False)
                usuario.rol = "Cliente"  # Rol predeterminado
                
                # Guardar la contraseña sin encriptar (NO RECOMENDADO)
                usuario.contraseña = data.get("contraseña")
                
                usuario.save()
                return JsonResponse({'message': 'Usuario creado exitosamente'}, status=201)
            else:
                return JsonResponse({'errors': form.errors}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Solicitud no válida. Formato JSON incorrecto.'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def VerUsuarios(request):
    if request.method == "GET":
        usuarios = Usuario.objects.all().values('id', 'nombre', 'correo', 'Ciudad', 'rol')
        usuarios_lista = list(usuarios)  # Convertir QuerySet a lista
        return JsonResponse({'usuarios': usuarios_lista}, status=200)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
@csrf_exempt
def registrar_habitacion(request):
    if request.method == 'POST':
        try:
            # Parsear el cuerpo de la solicitud como JSON
            data = json.loads(request.body)
            
            # Obtener los datos de la solicitud JSON
            piso = data.get('piso')
            nhabitacion = data.get('nhabitacion')
            estado = data.get('Estado', False)

            if piso is None or nhabitacion is None:
                return JsonResponse({'message': 'Los campos piso y nhabitacion son obligatorios'}, status=400)

            # Crear la nueva habitación
            nueva_habitacion = Habitacion(piso=piso, nhabitacion=nhabitacion, Estado=estado)
            nueva_habitacion.save()

            return JsonResponse({'message': 'Habitación registrada correctamente'}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Solicitud no válida. Formato JSON incorrecto.'}, status=400)
    
    return JsonResponse({'message': 'Método no permitido'}, status=405)


@csrf_exempt
def registrar_reserva(request):
    if request.method == 'POST':
        try:
            # Parsear el cuerpo de la solicitud como JSON
            data = json.loads(request.body)

            # Obtener los datos de la solicitud JSON
            nombre = data.get('nombre')
            correo = data.get('correo')
            contraseña = data.get('contraseña')
            piso = data.get('piso')
            nhabitacion = data.get('nhabitacion')

            # Verificar si los datos requeridos están presentes
            if not nombre or not correo or not contraseña or not piso or not nhabitacion:
                return JsonResponse({'message': 'Faltan datos obligatorios (nombre, correo, contraseña, piso, nhabitacion)'}, status=400)

            # Verificar si la habitación existe
            try:
                habitacion = Habitacion.objects.get(piso=piso, nhabitacion=nhabitacion)
            except Habitacion.DoesNotExist:
                return JsonResponse({'message': 'La habitación no existe'}, status=404)

            # Verificar si la habitación está ocupada
            if habitacion.Estado:
                return JsonResponse({'message': 'La habitación está ocupada'}, status=400)

            # Crear la reserva
            nueva_reserva = Reservas(nombre=nombre, correo=correo, contraseña=contraseña,
                                     piso=piso, nhabitacion=nhabitacion)  # No necesitamos el campo Estado aquí
            try:
                nueva_reserva.save()
            except Exception as e:
                return JsonResponse({'message': f'Error al guardar la reserva: {str(e)}'}, status=500)

            # Marcar la habitación como ocupada
            habitacion.Estado = True
            habitacion.save()

            return JsonResponse({'message': 'Reserva realizada correctamente'}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'message': 'Solicitud no válida. Formato JSON incorrecto.'}, status=400)
        except Exception as e:
            return JsonResponse({'message': f'Error inesperado: {str(e)}'}, status=500)
    return JsonResponse({'message': 'Método no permitido'}, status=405)


@csrf_exempt
def VerHabitaciones(request):
    if request.method == "GET":
        habitaciones = Habitacion.objects.all().values('piso', 'nhabitacion', 'Estado')
        habitaciones_lista = list(habitaciones)  # Convertir QuerySet a lista
        return JsonResponse({'habitaciones': habitaciones_lista}, status=200)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def VerReservas(request):
    if request.method == "GET":
        reservas = Reservas.objects.all().values('nombre', 'correo', 'piso', 'nhabitacion')
        reservas_lista = list(reservas)  # Convertir QuerySet a lista
        return JsonResponse({'reservas': reservas_lista}, status=200)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)


@csrf_exempt
def login(request):
    if request.method == "POST":
        try:
            # Parsear los datos de la solicitud JSON
            data = json.loads(request.body)
            correo = data.get('correo')
            contraseña = data.get('contraseña')

            # Verificar si el correo y la contraseña están presentes
            if not correo or not contraseña:
                return JsonResponse({'error': 'Correo y contraseña son obligatorios'}, status=400)

            # Buscar al usuario por correo
            try:
                usuario = Usuario.objects.get(correo=correo)
            except Usuario.DoesNotExist:
                return JsonResponse({'error': 'Usuario no encontrado'}, status=404)

            # Validar la contraseña
            if not check_password(contraseña, usuario.contraseña):
                return JsonResponse({'error': 'Contraseña incorrecta'}, status=401)

            # Retornar un mensaje de bienvenida en JSON
            return JsonResponse({'message': f'Bienvenido {usuario.correo}'}, status=200)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON no válido'}, status=400)

    # Si no es un método POST, retornar error
    return JsonResponse({'error': 'Método no permitido'}, status=405)