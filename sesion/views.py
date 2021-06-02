from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def index(request):
  """Redirección manual"""
  return inicio_sesion(request)

def inicio_sesion(request):
  """Módulo que permite al usuario
  registrarse e/o iniciar sesión.
  """
  # En caso de estar recibiendo datos
  # ocultos en la url del navegador.
  if request.method == 'POST':
    # Se rescatan los campos de usuario y contraseña.
    usuario = request.POST['username']
    contra = request.POST['password']

    # Se verifica que las crenciales sean válidas.
    usuarioLogeado = authenticate(username = usuario, password = contra)

    # Debiera devolver una instancia de sesión.
    # De lo contrario, devuelve 'None'.
    if usuarioLogeado is not None:

      # La función login() iniciará la sesión.
      login(request, usuarioLogeado)

      # Si la autenticación es correcta, 
      # entonces la plantilla se renderizará
      # como un usuario válidamente autenticado.
      return render(request, 'login.html', {'errores': 'TODO_BIEN'})
      
    # Si la autenticación falla, 
    # la sesión NO existirá.
    else:
      # Se verifica que exista el nombre de usuario en la base de datos.
      if len(User.objects.filter(username=usuario)):
        # Si existe, se le informa al usuario que la contraseña es incorrecta.
        return render(request, 'login.html', {'errores':'CONTRASEÑA_INCORRECTA'})
      else:
         # Si no existe, se le informa al usuario que el nombre de usuario no existe.
        return render(request, 'login.html', {'errores':'NO_EXISTE_NOMBRE_USUARIO'})

  # Página de inicio de sesión.
  return render(request, 'login.html')

def crear_usuario(request):
  """Registro para crear usuario"""

  # En caso de estar recibiendo datos
  # ocultos en la url del navegador.
  if request.method == 'POST':

    # Se rescatan los campos de usuario, contraseña y correo electrónico.
    usuario = request.POST['username']
    contra = request.POST['password']
    email = request.POST['email']

    # Se verifica que no exista el nombre de usuario en la base de datos.
    if User.objects.filter(username=usuario):
      # Si existe, se le informa al usuario que el nombre de usuario no está disponible.
      return render(request, 'login.html', {'mensaje':'YA_EXISTE_NOMBRE_USUARIO'})

    # Se procede a crear el usuario en la base de datos.
    nuevo_usuario = User.objects.create_user(username = usuario, password = contra, email = email)
    nuevo_usuario.save()

    # Se intenta iniciar sesión
    # con el usuario ya creado.
    login(request,nuevo_usuario)

    # Si la autenticación es correcta, 
    # entonces la plantilla se renderizará
    # como un usuario válidamente autenticado.
    return render(request, 'login.html', {'mensaje':'USUARIO_CREADO'})

  # En caso de haber algún error, se informa al usuario.
  return render(request, 'login.html', {'errores':'USUARIO_NO_CREADO'})

def cerrar_sesion(request):
  """Cierre de la sesión actual,
  redirección manual a la página 
  de inicio de sesión"""
  logout(request)
  return inicio_sesion(request)